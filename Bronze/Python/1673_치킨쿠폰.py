while True:
    try:
        n, k = map(int, input().split())

        chicken = 0
        coupon, stamp = n, 0
        while coupon > 0:
            chicken += coupon # 쿠폰이 있음, 치킨 주문
            stamp += coupon # 쿠폰 수 만큼 도장을 찍음
            coupon = 0
            if stamp >= k: # 도장을 교환할 수 있으면
                coupon += stamp//k # 바꿀 수 있을 만큼 쿠폰을 교환
                stamp -= (stamp//k)*k
        print(chicken) # 도장 교환 불가하면 먹은 치킨 수를 출력
    except EOFError:
        break