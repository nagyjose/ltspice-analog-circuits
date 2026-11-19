import matplotlib.pyplot as plt

def extract_all_traces(simulation_obj, plot=False):
    """
    Vrátí dict všech vektorů dat z objektu simulace.
    Pokud je 'plot=True', zobrazí dva subploty (napětí a proudy).

    Parameters:
        simulation_obj: objekt s metodami get_trace_names(), get_trace(name), get_axis()
        plot (bool): volitelný parametr pro zobrazení grafu

    Returns:
        dict: { trace_name (str): wave_data (list or array) }
    """
    trace_data = {}
    trace_names = simulation_obj.get_trace_names()
    x_axis = simulation_obj.get_axis()
    x_label = trace_names[0] if trace_names else "x"

    # Třídění do napětí a proudů
    voltage_traces = []
    current_traces = []

    for name in trace_names:
        trace = simulation_obj.get_trace(name)
        if trace is not None:
            wave = trace.get_wave()
            trace_data[name] = wave

            # Rozdělení podle typu
            if name.startswith("V("):
                voltage_traces.append((name, wave))
            elif name.startswith("I("):
                current_traces.append((name, wave))

    # Volitelné vykreslení
    if plot:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
        fig.suptitle("Simulační data")

        for name, wave in voltage_traces:
            ax1.plot(x_axis, wave, label=name)
        ax1.set_ylabel("Napětí [V]")
        ax1.grid(which='both', linestyle='--')
        ax1.margins(x=0)
        ax1.legend()

        for name, wave in current_traces:
            ax2.plot(x_axis, wave, label=name)
        ax2.set_ylabel("Proud [A]")
        ax2.set_xlabel(x_label)
        ax2.grid(which='both', linestyle='--')
        ax2.margins(x=0)
        ax2.legend()

        plt.tight_layout()
        plt.subplots_adjust(top=0.92)
        plt.show()

    return trace_data


def format_with_prefix(value, unit):
    """
    Převádí číselnou hodnotu s jednotkou na formátovaný string s odpovídající SI předponou.

    Parameters:
        value (float): hodnota (např. 8.35e6)
        unit (str): jednotka (např. 'V', 'A', 'Ohm')

    Returns:
        str: naformátovaný výstup, např. '8.35 MOhm', '120 µA'
    """
    prefixes = [
        (1e24, 'Y'),   # yotta
        (1e21, 'Z'),   # zetta
        (1e18, 'E'),   # exa
        (1e15, 'P'),   # peta
        (1e12, 'T'),   # tera
        (1e9,  'G'),   # giga
        (1e6,  'M'),   # mega
        (1e3,  'k'),   # kilo
        (1,    ''),    # jednotkový násobek
        (1e-3, 'm'),   # mili
        (1e-6, 'µ'),   # mikro
        (1e-9, 'n'),   # nano
        (1e-12,'p'),   # piko
        (1e-15,'f'),   # femto
        (1e-18,'a'),   # atto
        (1e-21,'z'),   # zepto
        (1e-24,'y')    # yocto
    ]

    abs_val = abs(value)

    for factor, prefix in prefixes:
        if abs_val >= factor:
            scaled = value / factor
            return f"{scaled:.3g} {prefix}{unit}"

    return f"{value:.3g} {unit}"

