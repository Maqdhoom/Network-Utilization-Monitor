from pox.core import core
import pox.openflow.libopenflow_01 as of
import time

log = core.getLogger()

# Store previous stats
prev_stats = {}

# Link capacity (in bits/sec)
LINK_CAPACITY = 10_000_000  # 10 Mbps


def _handle_portstats_received(event):
    global prev_stats

    dpid = event.connection.dpid
    now = time.time()

    for stat in event.stats:
        port = stat.port_no

        if port < 65534:  # ignore special ports
            key = (dpid, port)

            rx_bytes = stat.rx_bytes
            tx_bytes = stat.tx_bytes

            if key in prev_stats:
                old_rx, old_tx, old_time = prev_stats[key]

                interval = now - old_time

                rx_rate = (rx_bytes - old_rx) * 8 / interval
                tx_rate = (tx_bytes - old_tx) * 8 / interval

                utilization = ((rx_rate + tx_rate) / LINK_CAPACITY) * 100

                log.info("Switch %s Port %s | RX: %.2f Mbps TX: %.2f Mbps Util: %.2f%%",
                         dpid, port,
                         rx_rate / 1_000_000,
                         tx_rate / 1_000_000,
                         utilization)

            prev_stats[key] = (rx_bytes, tx_bytes, now)


def _timer_func():
    for connection in core.openflow._connections.values():
        connection.send(of.ofp_stats_request(body=of.ofp_port_stats_request()))
    core.callDelayed(1, _timer_func)


def launch():
    log.info("📡 POX Network Utilization Monitor Started")

    core.openflow.addListenerByName("PortStatsReceived",
                                   _handle_portstats_received)

    core.callDelayed(1, _timer_func)
