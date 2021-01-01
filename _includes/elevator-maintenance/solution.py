class Elevator:
    def __init__(self, elevator):
        div = list(map(int, elevator.strip().split('.')))
        self.str = elevator
        self.major = div[0]
        self.minor = div[1] if len(div) > 1 else -1
        self.revision = div[2] if len(div) > 2 else -1
        
    def __lt__(self, other):
        if self.major < other.major: return True
        if self.major > other.major: return False
        if self.minor < other.minor: return True
        if self.minor > other.minor: return False
        if self.revision < other.revision: return True
        if self.revision > other.revision: return False

def solution(l):
    els = []
    for elevator in l:
        els.append(Elevator(elevator))
    els.sort()
    return [el.str for el in els]

if __name__ == "__main__":
    l1 = {"1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"}
    print(solution(l1))

    l2 = {"1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"}
    print(solution(l2))