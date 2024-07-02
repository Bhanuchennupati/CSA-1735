person('Alice', date(1990, 5, 24)).
person('Bob', date(1985, 11, 16)).
person('Charlie', date(2000, 7, 10)).
find_dob(Name, DOB) :-
    person(Name, DOB).
add_person(Name, date(Year, Month, Day)) :-
    assertz(person(Name, date(Year, Month, Day))).
