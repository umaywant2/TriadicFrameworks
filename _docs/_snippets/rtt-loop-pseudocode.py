def rtt_loop():
    tick = 0
    while simulation_running():
        state = capture_state()
        packet = build_rttcode_packet(state, tick)
        rtt_out = rttcore.step(packet)
        apply_rtt_state(rtt_out)
        tick += 1

