# 17091번: 단어 시계 - <img src="https://static.solved.ac/tier_small/6.svg" style="height:20px" /> Silver V

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/17091)

<p>단어 시계는 시각을 단어를 이용해서 표현하는 시계이다. 다음은 몇 가지 예시이다.</p>

<ul>
<li>5:00&nbsp;→ five o' clock</li>
<li>5:01&nbsp;→ one minute past five</li>
<li>5:10&nbsp;→ ten minutes past five</li>
<li>5:15&nbsp;→ quarter past five</li>
<li>5:28 → twenty eight minutes past five</li>
<li>5:30&nbsp;→ half past five</li>
<li>5:40&nbsp;→ twenty minutes to six</li>
<li>5:45&nbsp;→ quarter to six</li>
<li>5:47&nbsp;→ thirteen minutes to six</li>
</ul>

<p>분 = 0이면&nbsp;"o' clock"을 사용하고, 1 ≤ 분 ≤ 30은 "past"를, 30 &lt; 분이면 "to" 를 사용한다.</p>

<p>시각이 주어졌을 때, 단어 시계에서 사용하는 표현으로 출력해보자.</p>

## 입력

<p>첫째 줄에 시를 나타내는 h(1 ≤ h ≤ 12), 둘째 줄에 분을 나타내는 m(0 ≤ m &lt; 60)이 주어진다.</p>

## 출력

<p>첫째 줄에 입력으로 주어진 시각을 단어 시계에서 사용하는 표현으로 출력한다.</p>

## 소스코드

[소스코드 보기](단어%20시계.py)