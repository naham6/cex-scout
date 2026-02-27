from models import curr
from scraper import MarketScraper
from storage import save_to_csv
#import os
#from dotenv import load_dotenv
#load_dotenv()


if __name__ == "__main__":
    cex_scraper = MarketScraper()
    target_url = "https://api.binance.com/api/v3/ticker/price"
    #"https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT" for BTC only
    target_coins = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT']#working with these 4 currencies.
    
    raw_data_list = cex_scraper.fetch_data(target_url)
    
    if raw_data_list:
        p = [] 
        
        for item in raw_data_list:
            if item['symbol'] in target_coins:
                new_token = curr(
                    symbol=item['symbol'],
                    price=float(item['price'])
                )
                p.append(new_token)
        
        print("Daily Market Report")
        #for_ai = "" 
        for t in p:
            t.display_info()
            #for_ai = for_ai + f"{t.symbol}: ${t.price:.4f}\n"

        save_to_csv(p)















        '''this would give us the result but we can feed it into an AI prompt to get a professional market summary. with,
        system_prompt = f"""
        You are an expert crypto market analyst. 
        Review the following live cryptocurrency data and provide a professional, 2 sentence 
        executive summary of the current market state for our research team.
        
        Live Data:
        {for_ai}
        """
        
        final_summary = "It would be based on what ai am i using"
        
        print("\nAI Summary")
        print(final_summary)'''



        #result = cex_scraper.fetch_data(target_url) for json data.