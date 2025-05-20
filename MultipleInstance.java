import java.util.Scanner;

class MultipleInstance {
    String name = "";
    int rollNumber = 0;
    int numSubjects = 0;
    int[] marks;
    int total = 0;
    double avg = 0.0;

    public void accept() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter student name: ");
        name = sc.nextLine();

        System.out.print("Enter student roll number: ");
        rollNumber = sc.nextInt();

        System.out.print("Enter number of subjects: ");
        numSubjects = sc.nextInt();

        marks = new int[numSubjects];
        for (int i = 0; i < numSubjects; i++) {
            System.out.print("Enter marks for subject " + (i + 1) + ": ");
            marks[i] = sc.nextInt();
            total += marks[i];
        }

        avg = (double) total / numSubjects;
    }

    public void display() {
        System.out.println("\nStudent name: " + name);
        System.out.println("Student roll number: " + rollNumber);
        System.out.println("Student marks:");
        for (int i = 0; i < numSubjects; i++) {
            System.out.println("Subject " + (i + 1) + ": " + marks[i]);
        }
        System.out.printf("Student average marks: %.2f\n", avg);
    }

    public static void main(String[] args) {
        MultipleInstance student = new MultipleInstance();
        student.accept();
        student.display();
    }
}

