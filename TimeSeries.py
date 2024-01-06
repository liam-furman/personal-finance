from abc import ABC, abstractmethod
from collections import deque

class TimeSeries(ABC):

    def __func_constr_rel_getitem(self, time, shift, allowed_shifts):
        if shift not in allowed_shifts:
            raise ValueError("Input must be added to dependancies.")
        return self.__getitem__(time + shift)
        
    def __init__(self, initial_values=None, **kwargs):
        self.__series = list()
        if initial_values:
            self.__series = initial_values 
        self.__time = len(self.__series)

        # TODO: Check aren't any kwargs that don't match to dependancies

        if self.dependancies:
            for name, allowed_shifts in self.dependancies.items():
                if any(shift > 0 for shift in allowed_shifts):
                    raise IndexError("My be dependant only on previous timesteps.")
                setattr(self, name, lambda shift: kwargs[name].__func_constr_rel_getitem(self.__time, shift, allowed_shifts))

    @property
    @abstractmethod
    def dependancies(self):
        pass

    def __getitem__(self, t):
        if t < 0:
            raise ValueError("Absolute time indices for TimeSeries must be >= 0")
        return self.__series[t]

    def update(self):
        self.__series.append(self.__calculate__()) 
        self.__time += 1

    def __str__(self):
        return str(self.__series)
    
    @abstractmethod
    def __calculate__(self):
        pass

if __name__ == "__main__":
    
    class Age(TimeSeries):

        def __calculate__(self):
            # TODO: Make a neat, consistent method for reference self 
            # return self[-1]
            # return self[-1] + age_(t-1)#age(-1) + age(0)
            return self[self._TimeSeries__time - 1] + 1

        @property
        def dependancies(self):
            return None

    class Expenses(TimeSeries):

        def __calculate__(self):
            return self.age(-1) * 100

        @property
        def dependancies(self):
            return {
                'age': [-1],
            }

    age = Age(initial_values=[36])
    age.update()
    expenses = Expenses(initial_values=[3500], age=age)
    expenses.update()
    print(expenses)