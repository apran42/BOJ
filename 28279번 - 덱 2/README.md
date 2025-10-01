# 28279번: 덱 2 - <img src="https://static.solved.ac/tier_small/7.svg" style="height:20px" /> Silver IV

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/28279)

<p>정수를 저장하는 덱을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.</p>

<p>명령은 총 여덟 가지이다.</p>

<ol>
<li><span style="color:#e74c3c;"><code>1 X</code></span>: 정수 <var>X</var>를 덱의 앞에 넣는다. (1 ≤ <var>X</var> ≤ 100,000)</li>
<li><span style="color:#e74c3c;"><code>2 X</code></span>: 정수 <var>X</var>를 덱의 뒤에 넣는다. (1 ≤ <var>X</var> ≤ 100,000)</li>
<li><span style="color:#e74c3c;"><code>3</code></span>: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
<li><span style="color:#e74c3c;"><code>4</code></span>: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
<li><span style="color:#e74c3c;"><code>5</code></span>: 덱에 들어있는 정수의 개수를 출력한다.</li>
<li><span style="color:#e74c3c;"><code>6</code></span>: 덱이 비어있으면 <span style="color:#e74c3c;"><code>1</code></span>, 아니면 <span style="color:#e74c3c;"><code>0</code></span>을 출력한다.</li>
<li><span style="color:#e74c3c;"><code>7</code></span>: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
<li><span style="color:#e74c3c;"><code>8</code></span>: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
</ol>

## 입력

<p>첫째 줄에 명령의 수 <var>N</var>이 주어진다. (1 ≤ <var>N</var> ≤ 1,000,000)</p>

<p>둘째 줄부터 <var>N</var>개 줄에 명령이 하나씩 주어진다.</p>

<p>출력을 요구하는 명령은 하나 이상 주어진다.</p>

## 출력

<p>출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.</p>

## 소스코드

[소스코드 보기](덱%202.py)