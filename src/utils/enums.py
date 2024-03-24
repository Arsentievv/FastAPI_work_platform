from enum import Enum


class Workload(Enum):
    fulltime = "fulltime"
    parttime = "parttime"


class Grade(Enum):
    bachelor = "bachelor"
    master = "master"
    professional = "professional"
