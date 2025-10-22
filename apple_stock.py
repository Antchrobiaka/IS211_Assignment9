from bs4 import BeautifulSoup
def scrape_apple_stock():
    html_data = """
    <table>
        <tr><th>Date</th><th>Open</th><th>High</th><th>Low</th><th>Close</th><th>Adj Close</th><th>Volume</th></tr>
        <tr><td>Jul 22, 2025</td><td>213.14</td><td>214.95</td><td>212.23</td><td>214.40</td><td>214.16</td><td>46,404,100</td></tr>
        <tr><td>Jul 21, 2025</td><td>212.10</td><td>215.78</td><td>211.63</td><td>212.48</td><td>212.24</td><td>51,377,400</td></tr>
        <tr><td>Jul 18, 2025</td><td>210.87</td><td>211.79</td><td>209.70</td><td>211.18</td><td>210.94</td><td>48,974,600</td></tr>
        <tr><td>Jul 17, 2025</td><td>210.57</td><td>211.80</td><td>209.59</td><td>210.02</td><td>209.78</td><td>48,068,100</td></tr>
        <tr><td>Jul 16, 2025</td><td>210.30</td><td>212.40</td><td>208.64</td><td>210.16</td><td>209.92</td><td>47,490,500</td></tr>
        <tr><td>Jul 15, 2025</td><td>209.22</td><td>211.89</td><td>208.92</td><td>209.11</td><td>208.87</td><td>42,296,300</td></tr>
        <tr><td>Jul 14, 2025</td><td>209.93</td><td>210.91</td><td>207.54</td><td>208.62</td><td>208.38</td><td>38,840,100</td></tr>
        <tr><td>Jul 11, 2025</td><td>210.57</td><td>212.13</td><td>209.86</td><td>211.16</td><td>210.92</td><td>39,765,800</td></tr>
        <tr><td>Jul 10, 2025</td><td>210.51</td><td>213.48</td><td>210.03</td><td>212.41</td><td>212.17</td><td>44,443,600</td></tr>
        <tr><td>Jul 9, 2025</td><td>209.53</td><td>211.33</td><td>207.22</td><td>211.14</td><td>210.90</td><td>48,749,400</td></tr>
        <tr><td>Jul 8, 2025</td><td>210.10</td><td>211.43</td><td>208.45</td><td>210.01</td><td>209.77</td><td>42,848,900</td></tr>
        <tr><td>Jul 7, 2025</td><td>212.68</td><td>216.23</td><td>208.80</td><td>209.95</td><td>209.71</td><td>50,229,000</td></tr>
        <tr><td>Jul 3, 2025</td><td>212.15</td><td>214.65</td><td>211.81</td><td>213.55</td><td>213.31</td><td>34,955,800</td></tr>
        <tr><td>Jul 2, 2025</td><td>208.91</td><td>213.34</td><td>208.14</td><td>212.44</td><td>212.20</td><td>67,941,800</td></tr>
        <tr><td>Jul 1, 2025</td><td>206.67</td><td>210.19</td><td>206.14</td><td>207.82</td><td>207.58</td><td>78,788,900</td></tr>
        <tr><td>Jun 30, 2025</td><td>202.01</td><td>207.39</td><td>199.26</td><td>205.17</td><td>204.94</td><td>91,912,800</td></tr>
        <tr><td>Jun 27, 2025</td><td>201.89</td><td>203.22</td><td>200.00</td><td>201.08</td><td>200.85</td><td>73,188,600</td></tr>
    </table>
    """
    soup = BeautifulSoup(html_data, "html.parser")
    rows = soup.find_all("tr")[1:]
    print("\n💹 Apple (AAPL) Historical Stock Prices (Sample Data)\n")
    print(f"{'Date':<15}{'Close Price':<10}{'Volume':<15}")
    print("-" * 40)
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 7:
            date = cols[0].text.strip()
            close = cols[4].text.strip()
            volume = cols[6].text.strip()
            print(f"{date:<15}{close:<10}{volume:<15}")
if __name__ == "__main__":
    scrape_apple_stock()
