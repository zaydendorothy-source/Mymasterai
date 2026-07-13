from ddgs import DDGS


class WebSearch:

    def search(self, query, results=5):

        output = []

        try:

            with DDGS() as ddgs:

                search = ddgs.text(query, max_results=results)

                for item in search:

                    output.append({
                        "title": item.get("title", ""),
                        "body": item.get("body", ""),
                        "url": item.get("href", "")
                    })

        except Exception as e:

            output.append({
                "title": "Search Error",
                "body": str(e),
                "url": ""
            })

        return output


if __name__ == "__main__":

    web = WebSearch()

    while True:

        query = input("\nSearch > ")

        if query.lower() == "exit":
            break

        results = web.search(query)

        print()

        for i, item in enumerate(results, start=1):

            print("=" * 70)
            print(f"{i}. {item['title']}")
            print()
            print(item["body"])
            print()
            print(item["url"])
            print("=" * 70)