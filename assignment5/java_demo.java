import java.util.Calendar;
import java.util.Date;

//This is my highlighter for Java code

public class MyClass {
	static void myMethod() {
		System.out.println("I just got executed!");

		boolean isJavaFun = true;
		boolean isFishTasty = false;

		for (int i = 0; i < 10; i++) {
			if (i == 4) {
				continue;
			}
		}

		for (int i = 0; i < 10; i++) {
			if (i == 4) {
				break;
			}
			System.out.println(i);
		}

		String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
		for (String i : cars) {
			System.out.println(i);
		}

		int i = 0;
		while (i < 5) {
			System.out.println(i);
			i++;
		}

		int time = 22;
		if (time < 10) {
			System.out.println("Good morning.");
		} else if (time < 20) {
			System.out.println("Good day.");
		} else {
			System.out.println("Good evening.");
		}

		public static void main(String[] args) {
			myMethod();
		}
	}
