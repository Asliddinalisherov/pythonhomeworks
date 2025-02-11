universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    student_enrollment = [univ[1] for univ in universities]
    tuition_fees = [univ[2] for univ in universities]
    return student_enrollment, tuition_fees

def mean(values):
    return sum(values) / len(values)

def median(values):
    sorted_values = sorted(values)
    n = len(values)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_values[middle - 1] + sorted_values[middle]) / 2
    else:
        return sorted_values[middle]


student_enrollment, tuition_fees = enrollment_stats(universities)

total_students = sum(student_enrollment)
total_tuition = sum(tuition_fees)

student_mean = mean(student_enrollment)
student_median = median(student_enrollment)

tuition_mean = mean(tuition_fees)
tuition_median = median(tuition_fees)


print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")

print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}\n")

print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")

