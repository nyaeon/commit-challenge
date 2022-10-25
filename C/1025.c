#include <stdio.h>
int main() {
	int list[7] = { 10,20,40,50,60,70};
	int i, data, inx;
	printf("삽입 원소: ");
	scanf_s("%d", &data);

	// 원소가 들어갈 위치 찾기 : inx 변수
	if (data < list[0]) inx = 0;
	else {
		for (i = 0; i < 6; i++) {
			if (list[i] <= data && data <= list[i + 1]) {
				inx = i + 1;
				break;
			}
		}
	
	if (i == 6) inx = i;
	}

	// 마지막원소부터 inx 위치가 변수까지 뒤로 이동
	for (i = 6; i >= inx; i--)
		list[i] = list[i - 1];

	// inx 위치에 삽입할 원소 넣기
	list[inx] = data;

	// 선형리스트 출력
	for (i = 0; i < 7; i++)
		printf("%d\t", list[i]);
	printf("\n\n");
	printf("========삭제 알고리즘========\n");
	printf("삭제원소: ");
	scanf_s("%d", &data);

	// 삭제할 원소의 위치 파악 : inx 변수 --> 못찾으면 오류 메세지     #5
	for (i = 0; i < 7; i++)
		if (list[i] == data) {
			inx = i;
			break;
		}

	if (i == 7) printf("삭제할 원소를 찾지 못했습니다");
	else {
		//inx+1 원소부터 마지막 원소까지 앞으로 한칸씩 이동
		for (i = inx; i < 6; i++)
			list[i] = list[i + 1];
		list[i] = 0;
	}
	

	//출력
	for (i = 0; i < 7; i++)
		printf("%d\t", list[i]);
	printf("\n\n");

}