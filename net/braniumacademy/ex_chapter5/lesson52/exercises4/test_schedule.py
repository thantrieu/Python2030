class TestSchedule:
    """This class describe test schedule info and behaviors."""

    def __init__(self, sid, time, date, room, subject, num_of_student):
        self.id = sid
        self.time = time
        self.date = date
        self.room = room
        self.subject = subject
        self.num_of_student = num_of_student
