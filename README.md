# DFA Minimization Tool

This project implements a Deterministic Finite Automaton (DFA) minimization tool in Python. The program allows users to define a DFA and then generates its minimized equivalent using state reduction algorithms. It also provides a user-friendly interface to input states, alphabet, transition functions, start state, and accept states.

## Features
- **State Reachability Analysis**: Identifies and removes unreachable states from the DFA.
- **State Minimization**: Reduces the DFA to its minimal form using equivalence class partitioning.
- **Interactive Input**: Guides users to input valid DFA components with real-time error handling.
- **Visual Output**: Displays the original and minimized DFA in a human-readable format.

## How to Run
1. **Install Python**: Make sure Python 3.x is installed on your system.
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/bedirhancan/dfa_minimize
   cd dfa_minimize
   ```
3. **Run the Program**:
   ```bash
   python dfa.py
   ```

## Input Format
1. **States**: Provide the number of states and their names as alphanumeric strings separated by commas.
2. **Alphabet**: Provide the size of the alphabet and its symbols as single characters separated by commas.
3. **Transition Function**: Define transitions for each state and symbol.
4. **Start State**: Provide the starting state name.
5. **Accept States**: Provide the accept states as a comma-separated list.

### Example Input
```
Kaç adet durum gireceksiniz? 3
Alfabedeki sembol sayısı nedir? 2
3 durum giriniz (virgülle ayırın): q0,q1,q2
2 sembol giriniz (virgülle ayırın): 0,1
q0 durumundan 0 sembolü ile geçilen durum: q1
q0 durumundan 1 sembolü ile geçilen durum: q2
q1 durumundan 0 sembolü ile geçilen durum: q0
q1 durumundan 1 sembolü ile geçilen durum: q2
q2 durumundan 0 sembolü ile geçilen durum: q1
q2 durumundan 1 sembolü ile geçilen durum: q2
Başlangıç durumunu giriniz: q0
Kabul durumlarını giriniz (virgülle ayırın): q2
```

### Example Output
Original DFA:
```
Durumlar: ['q0', 'q1', 'q2']
Alfabe: {'0', '1'}
Geçiş Fonksiyonu:
  q0 --0--> q1
  q0 --1--> q2
  q1 --0--> q0
  q1 --1--> q2
  q2 --0--> q1
  q2 --1--> q2
Başlangıç Durumu: {'q0'}
Kabul Durumları: {'q2'}
```

Minimized DFA:
```
Durumlar: ['q0', 'q2']
Alfabe: {'0', '1'}
Geçiş Fonksiyonu:
  q0 --0--> q0
  q0 --1--> q2
  q2 --0--> q0
  q2 --1--> q2
Başlangıç Durumu: {'q0'}
Kabul Durumları: {'q2'}
```

## Requirements
- Python 3.x
- No additional libraries are required.

## License
This project is licensed under the MIT License.

## Author
**Bedirhan CAN**
