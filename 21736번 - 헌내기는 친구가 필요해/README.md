# 21736번: 헌내기는 친구가 필요해 - <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" style="height:20px" /> Silver II

<!-- performance -->
### 성능 요약
메모리: 41544 KB, 시간: 1128 ms
<!-- end -->

## 문제

[문제 링크](https://boj.kr/21736)

<p>2020년에 입학한 헌내기 도연이가 있다. 도연이는 비대면 수업 때문에 학교에&nbsp;가지 못해 학교에 아는 친구가 없었다. 드디어 대면 수업을 하게 된 도연이는 어서 캠퍼스 내의 사람들과 친해지고 싶다.&nbsp;</p>

<p>도연이가 다니는 대학의 캠퍼스는 $N \times M$ 크기이며&nbsp;캠퍼스에서 이동하는&nbsp;방법은 벽이 아닌 상하좌우로 이동하는 것이다. 예를 들어, 도연이가 ($x$, $y$)에 있다면 이동할 수 있는 곳은 ($x+1$, $y$), ($x$, $y+1$), ($x-1$, $y$), ($x$, $y-1$)이다. 단, 캠퍼스의 밖으로 이동할 수는 없다.</p>

<p>불쌍한 도연이를 위하여 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하는 프로그램을 작성해보자.</p>

## 입력

<p>첫째 줄에는 캠퍼스의 크기를 나타내는 두 정수 $N$ ($ 1 \leq N \leq 600$), $M$ ($ 1 \leq M&nbsp;\leq 600$)이 주어진다.</p>

<p>둘째 줄부터 $N$개의 줄에는 캠퍼스의 정보들이 주어진다. <span style="color:#e74c3c;"><code>O</code></span>는 빈 공간, <span style="color:#e74c3c;"><code>X</code></span>는 벽, <span style="color:#e74c3c;"><code>I</code></span>는 도연이, <span style="color:#e74c3c;"><code>P</code></span>는 사람이다. <span style="color:#e74c3c;"><code>I</code></span>가 한 번만 주어짐이 보장된다.</p>

## 출력

<p>첫째 줄에 도연이가 만날 수 있는 사람의 수를 출력한다. 단, 아무도 만나지 못한 경우 <span style="color:#e74c3c;"><code>TT</code></span>를 출력한다.</p>

## 소스코드

[소스코드 보기](헌내기는%20친구가%20필요해.py)