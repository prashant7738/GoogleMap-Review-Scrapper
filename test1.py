from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import datetime
import time
import random
import re

url = "https://www.google.com/maps/?hl=en"


def googlemap_scrapper():

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=r"/home/prashant/Coding/Projects/GoogleMapReviewScrapper/user",
            channel="chrome",
            no_viewport=True,
            headless=False,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
            locale="en-US",
            extra_http_headers={
                "Accept-Language": "en-US,en;q=0.9" # Tells the server "Only send me English"
            },
            args=["--start-maximized","--lang=en-US"],
            proxy=None  # Add proxy support if needed
        )

        context.add_init_script("""
            Object.defineProperty(navigator,'webdriver',{get:() => undefined});
            window.chrome = {runtime:{}};
            Object.defineProperty(navigator,'plugins',{get:() => [1,2,3,4,5]});
            Object.defineProperty(navigator,'languages',{get:() => ['en-US','en']});
        """)

        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded")
        reviews_data = []

        try:
            
            page.get_by_role("combobox").fill('hotel near biratnagar')
            page.keyboard.press("Enter")

             # Wait for results panel
            results_panel = page.locator('div[role="feed"]')
            results_panel.wait_for(timeout=50000)

            # # Scroll to load more results
            # for _ in range(10):
            #     results_panel.evaluate("el => el.scrollBy(0, el.scrollHeight)")
            #     page.wait_for_timeout(1000)


            articles_locator = page.get_by_role("article")
            # articles_locator.first.wait_for(timeout = 50000)

            articles = articles_locator.all()
            print(f"Found {len(articles)} articles")

            for article in articles:
                
                business_name = article.locator(".fontHeadlineSmall").first.inner_text()
                print(f"\nProcessing: {business_name}")
                article.click()

                

                review_button = page.get_by_role("tab", name=re.compile(r"Reviews", re.IGNORECASE))
                review_button.wait_for(state='visible',timeout=25000)
                review_button.click()

                # 3. Wait for the review list to actually load
                # page.locator(".MyEned").first.wait_for(state='visible', timeout=10000)
                page.locator(".GHT2ce").first.wait_for(state='visible', timeout=10000)

                
                for _ in range(3):
                    page.mouse.wheel(0, 1000) # Simple way to scroll the active panel
                    page.wait_for_timeout(2000)


                # review_cards = page.locator('div[role="article"]', has=page.locator(".MyEned")).all()
                review_cards = page.locator('.GHT2ce').all()
                print(f"Found {len(review_cards)} review cards for {business_name}")


                

                for review in review_cards:
                    try:
                        # Extract rating from aria-label
                        rating_elem = review.locator('span[role="img"]').first
                        rating_text = rating_elem.get_attribute('aria-label') if rating_elem.count() else "0 stars"
                        rating = re.search(r'(\d+\.?\d*)\s*stars?', rating_text)
                        rating = rating.group(1) if rating else "0"
                        
                    
                        # Extract review text
                        review_text = review.locator(".MyEned").inner_text() if review.locator(".MyEned").count() else ""
                        
                        # Extract date with timeout handling
                        try:
                            date = review.locator("xpath=.//span[contains(text(), 'ago')]").inner_text(timeout=5000)
                        except:
                            date = ""
                        
                        # Only append if we have review text
                        if review_text:
                            reviews_data.append({
                                'review': review_text,
                                'rating': rating,
                                'date': date
                            })

                    except Exception as e:
                        print(f'Error extracting review: {e}')


        except Exception as e:
            print(f"Scraping interrupted: {e}")
        
        finally:
            # Save data to CSV (runs whether scraping succeeds or fails)
            if reviews_data:
                df = pd.DataFrame(reviews_data)
                csv_filename = 'googlemaphotelreview.csv'
                
                try:
                    existing_df = pd.read_csv(csv_filename)
                    df = pd.concat([existing_df, df], ignore_index=True)
                except FileNotFoundError:
                    pass
                
                df.to_csv(csv_filename, index=False)
                print(f"✓ Total reviews scraped: {len(reviews_data)}")
                print(f"✓ Data saved to {csv_filename}")
            else:
                print("✗ No reviews were scraped")

            context.close()
            print("Script completed.")

googlemap_scrapper()