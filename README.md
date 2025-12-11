# seoul_weather_5_m
@app.route("/index")
def index():
    # 1) 사용자 입력 도시명 받기
    city = request.args.get("city", "서울특별시")

    # 2) 도시명 → 도시ID 매핑
    city_id = city_name_to_id.get(city)

    # 3) OpenWeather API URL 구성
    api_key = "YOUR_OPENWEATHER_API_KEY"
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?id={city_id}"
        f"&appid={api_key}&units=metric"
    )

    # 4) API 호출
    response = requests.get(url).json()
    weather = response["weather"][0]["main"]   # Clear, Clouds, Rain...
    temp = round(response["main"]["temp"], 1)

    # 5) 날씨 → 키워드 변환
    keyword = convert_weather_to_keyword(weather)

    # 6) 멜론 DJ 검색 및 플레이리스트 크롤링
    playlist_links = search_melon_dj(keyword)
    selected_playlist = random.choice(playlist_links)

    # 7) 해당 플레이리스트에서 랜덤 3곡 추출
    songs = crawl_playlist(selected_playlist)

    # 8) 결과 페이지 렌더링
    return render_template(
        "index.html",
        city=city,
        weather=weather,
        temp=temp,
        songs=songs,
    )
