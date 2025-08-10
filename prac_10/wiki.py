import wikipedia


def main():
    wikipedia.set_lang("en")  # optional: ensure English results
    query = input("Enter page title (blank to quit): ").strip()

    while query:
        try:
            # Attempt to fetch the page with the given query
            page = wikipedia.page(query, auto_suggest=False)
            print(f"\n{page.title}\n{page.summary[:500]}...\n{page.url}\n")

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or search again:")
            # Show a shorter list so it’s not overwhelming
            options = e.options[:15]
            for i, opt in enumerate(options, start=1):
                print(f"{i}. {opt}")

        except wikipedia.exceptions.PageError:
            print(f'Page title "{query}" does not match any pages. Try another title!')

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        query = input("\nEnter page title (blank to quit): ").strip()

    print("Thank you.")


if __name__ == "__main__":
    main()
