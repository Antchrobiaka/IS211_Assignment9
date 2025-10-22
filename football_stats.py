from bs4 import BeautifulSoup
def scrape_football_stats():
    html_data = """
    <table>
        <tr>
            <th>Rank</th><th>Team</th><th>Player</th><th>Pos</th><th>PTS</th>
        </tr>
        <tr>
            <td>T1</td><td>DAL</td><td>Brandon Aubrey</td><td>K</td><td>68</td>
        </tr>
        <tr>
            <td>T1</td><td>IND</td><td>Jonathan Taylor</td><td>RB</td><td>68</td>
        </tr>
        <tr>
            <td>3</td><td>SEA</td><td>Jason Myers</td><td>K</td><td>61</td>
        </tr>
        <tr>
            <td>4</td><td>SF</td><td>Eddy Pineiro</td><td>K</td><td>60</td>
        </tr>
        <tr>
            <td>5</td><td>LAC</td><td>Cameron Dicker</td><td>K</td><td>59</td>
        </tr>
    </table>
    """
    soup = BeautifulSoup(html_data, "html.parser")
    rows = soup.find_all("tr")[1:]  
    print("\n🏈 Top NFL Scoring Leaders (Sample Data)\n")
    print(f"{'Rank':<5}{'Team':<8}{'Player':<25}{'Pos':<5}{'PTS':<5}")
    print("-" * 55)
    for row in rows:
        cols = row.find_all("td")
        rank = cols[0].text.strip()
        team = cols[1].text.strip()
        player = cols[2].text.strip()
        position = cols[3].text.strip()
        points = cols[4].text.strip()

        print(f"{rank:<5}{team:<8}{player:<25}{position:<5}{points:<5}")
if __name__ == "__main__":
    scrape_football_stats()
