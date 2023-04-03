#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	double g_sum = 0, c_sum = 0;
	for (int i = 0; i < 20; i++) {
		char subject[51], grade[3] = { "", };
		double credit;
		scanf("%s %lf %s", subject, &credit, grade);
		if (grade[0] != 'P') {
			c_sum += credit;
			switch (grade[0])
			{
			case 'A':
				g_sum += 4.0 * credit; break;
			case 'B':
				g_sum += 3.0 * credit; break;
			case 'C':
				g_sum += 2.0 * credit; break;
			case 'D':
				g_sum += 1.0 * credit; break;
			default:
				break;
			}
			if (grade[1] == '+')
				g_sum += 0.5 * credit;
		}
	}
	printf("%lf", g_sum / c_sum);
}