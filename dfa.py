import re

class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def get_reachable_states(self):
        reachable = {self.start_state}
        changed = True
        while changed:
            changed = False
            for state in list(reachable):
                for symbol in self.alphabet:
                    next_state = self.transition_function.get(state, {}).get(symbol)
                    if next_state and next_state not in reachable:
                        reachable.add(next_state)
                        changed = True
        return reachable

    def remove_unreachable_states(self):
        reachable = self.get_reachable_states()
        new_states = list(reachable)
        new_accept_states = {state for state in self.accept_states if state in reachable}
        new_transition_function = {}
        
        for state in reachable:
            if state in self.transition_function:
                new_transition_function[state] = {}
                for symbol, next_state in self.transition_function[state].items():
                    if next_state in reachable:
                        new_transition_function[state][symbol] = next_state

        return DFA(new_states, self.alphabet, new_transition_function, self.start_state, new_accept_states)

    def minimize(self):
        dfa = self.remove_unreachable_states()
        
        P = [set(dfa.accept_states), set(dfa.states) - set(dfa.accept_states)]
        W = [set(dfa.accept_states), set(dfa.states) - set(dfa.accept_states)]
        
        while W:
            A = W.pop(0)
            for c in dfa.alphabet:
                predecessors = set()
                for state in dfa.states:
                    if state in dfa.transition_function and c in dfa.transition_function[state]:
                        if dfa.transition_function[state][c] in A:
                            predecessors.add(state)
                
                for Y in list(P):
                    intersection = Y & predecessors
                    difference = Y - predecessors
                    if intersection and difference:
                        P.remove(Y)
                        P.extend([intersection, difference])
                        if Y in W:
                            W.remove(Y)
                            W.extend([intersection, difference])
                        else:
                            if len(intersection) <= len(difference):
                                W.append(intersection)
                            else:
                                W.append(difference)

        new_states = []
        new_transition_function = {}
        state_mapping = {}

        for equivalence_class in P:
            new_state = frozenset(equivalence_class)
            new_states.append(new_state)
            for state in equivalence_class:
                state_mapping[state] = new_state

        for new_state in new_states:
            new_transition_function[new_state] = {}
            representative = next(iter(new_state))
            for symbol in dfa.alphabet:
                if representative in dfa.transition_function and symbol in dfa.transition_function[representative]:
                    next_state = dfa.transition_function[representative][symbol]
                    new_transition_function[new_state][symbol] = state_mapping[next_state]

        new_start_state = state_mapping[dfa.start_state]
        new_accept_states = {state_mapping[state] for state in dfa.accept_states}

        return DFA(new_states, dfa.alphabet, new_transition_function, new_start_state, new_accept_states)

    def print_dfa(self):
        def format_state(state):
            if isinstance(state, frozenset):
                return ','.join(state)
            return state

        print("Durumlar:", [format_state(state) for state in self.states])
        print("Alfabe:", self.alphabet)
        print("Geçiş Fonksiyonu:")
        for state, transitions in self.transition_function.items():
            for symbol, next_state in transitions.items():
                print(f"  {format_state(state)} --{symbol}--> {format_state(next_state)}")
        print("Başlangıç Durumu:", {format_state(self.start_state)})
        print("Kabul Durumları:", {format_state(state) for state in self.accept_states})

# Kullanıcıdan veri alma
while True:
    durum_sayisi = input("Kaç adet durum gireceksiniz? ")
    if durum_sayisi.isdigit() and int(durum_sayisi) > 0:
        durum_sayisi = int(durum_sayisi)
        break
    print("Hata: Lütfen geçerli bir pozitif tam sayı girin!")

while True:
    alfabe_boyutu = input("Alfabedeki sembol sayısı nedir? ")
    if alfabe_boyutu.isdigit() and int(alfabe_boyutu) > 0:
        alfabe_boyutu = int(alfabe_boyutu)
        break
    print("Hata: Lütfen geçerli bir pozitif tam sayı girin!")

# Durumların alınması
while True:
    print(f"{durum_sayisi} durum giriniz (virgülle ayırın):")
    states = input("Durumları girin: ").split(',')
    if len(states) == durum_sayisi:
        if len(set(states)) != len(states):
            print("Hata: Durumlar benzersiz olmalıdır!")
            continue
        invalid_states = [state for state in states if not re.match("^[a-zA-Z0-9]+$", state)]
        if invalid_states:
            print(f"Hata: Şu durumlar geçersiz karakterler içeriyor: {', '.join(invalid_states)}")
            continue
        states = set(states)
        break
    print(f"Hata: {durum_sayisi} adet durum girmelisiniz!")

# Alfabe sembollerinin alınması
while True:
    print(f"{alfabe_boyutu} sembol giriniz (virgülle ayırın):")
    alphabet = input("Alfabeyi girin: ").split(',')
    if len(alphabet) == alfabe_boyutu:
        if len(set(alphabet)) != len(alphabet):
            print("Hata: Alfabe sembolleri benzersiz olmalıdır!")
            continue
        invalid_symbols = [symbol for symbol in alphabet if not re.match("^[a-zA-Z0-9]$", symbol)]
        if invalid_symbols:
            print(f"Hata: Şu semboller geçersiz: {', '.join(invalid_symbols)}")
            continue
        alphabet = set(alphabet)
        break
    print(f"Hata: {alfabe_boyutu} adet sembol girmelisiniz!")

# Geçiş fonksiyonunun alınması
transition_function = {}
print("Geçiş fonksiyonunu giriniz:")
for state in states:
    transition_function[state] = {}
    for symbol in alphabet:
        while True:
            next_state = input(f"{state} durumundan {symbol} sembolü ile geçilen durum: ")
            if next_state in states:
                transition_function[state][symbol] = next_state
                break
            print(f"Hata: {next_state} durumu belirtilen durumlar arasında değil!")

# Başlangıç durumunun alınması
while True:
    start_state = input("Başlangıç durumunu giriniz: ")
    if start_state in states:
        break
    print(f"Hata: Başlangıç durumu, girdiğiniz durumlar arasında olmalıdır!")

# Kabul durumlarının alınması
while True:
    accept_states = input("Kabul durumlarını giriniz (virgülle ayırın): ").split(',')
    accept_states = set(accept_states)
    if accept_states.issubset(states):
        break
    print(f"Hata: Kabul durumları, girdiğiniz durumlar arasında olmalıdır!")

# DFA oluşturma
dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

# Orijinal DFA'yı yazdırma
print("\nOrijinal DFA:")
dfa.print_dfa()

# Minimize edilmiş DFA
minimized_dfa = dfa.minimize()

# Minimize edilmiş DFA'yı yazdırma
print("\nMinimize Edilmiş DFA:")
minimized_dfa.print_dfa()

input("Çıkmak için Enter'a basın...")

