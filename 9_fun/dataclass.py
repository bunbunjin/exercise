from dataclasses import dataclass


@dataclass(frozen=True)
class Profile:
    name: str
    age: int
    sex: str
    school: str


profile = Profile(name='bunbunjin', age=18, sex='man', school='OUS')


@dataclass()
class School:

    def output(self):
        return f'{self.where}にある{self.name}'


s = School()
s.where = 'Okayama'
s.name = 'OUS'
print(s.output())
s.where = 'Ridai city'
print(s.output())
