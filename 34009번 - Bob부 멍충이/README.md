# 34009번: Bob부 멍충이 - <img src="https://static.solved.ac/tier_small/4.svg" style="height:20px" /> Bronze II

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/34009)

<p>Alice와 Bob이 길이가 $N$인 서로 다른 양의 정수로 이루어진 수열 $A_1, A_2, \cdots , A_N$에서 게임을 진행한다. 현재 수열에 남은 원소의 개수가 짝수라면, Alice의 점수가 $A_1$만큼 증가하고, 홀수라면 Bob의 점수가 $A_1$만큼 증가한다. 이후 수열에서 $A_1$은 제거된다. 수열이 비게 되면 게임이 종료된다.</p>

<p>게임을 시작하기 전을 제외한 모든 순간에 Alice의 점수가 Bob의 점수보다 크다면 Alice가 이긴다. 그렇지 않은 순간이 한 번이라도 존재하면 Bob이 이긴다. 이때, 배열을 적절하게 섞어서 Alice가 이길 수 있는지 알아보자.</p>

## 입력

<p>첫째 줄에 수열 $A$의 크기 $N$이 주어진다. $(1 \le N \le 10^5)$</p>

<p>둘째 줄에 $A_1, A_2, \cdots , A_N$이 공백으로 구분되어 주어진다. $(1 \le A_i \le 10^9)$</p>

<p>$A_i$는 <strong>서로 다르며</strong>, 입력으로 주어지는 모든 수는 정수이다.</p>

## 출력

<p>Alice가 이길 수 있도록 배열을 섞을 수 있는 경우 <span style="color:#e74c3c;"><code>Alice</code></span>를, 그렇지 않은 경우 <span style="color:#e74c3c;"><code>Bob</code></span>을 출력한다.</p>

## 소스코드

[소스코드 보기](Bob부%20멍충이.py)