
from . import fileparse
from .stock import Stock
from .portfolio import Portfolio
from . import tableformat

def read_portfolio(filename,**opts):
    '''
    Read a portfolio file and return a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)
    
def read_prices(filename):
    '''
    Read a CSV file with price data and return a dictionary mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))

def make_report_data(portfolio,prices):
    '''
    Create a list of tuples (name, shares, price, change) based on the portfolio list
    and the prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata,formatter):
    '''
    Print a nicely formatted table from a list of tuples (name, shares, price, change).
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile,fmt=None):        
    '''
    Generate a stock report based on portfolio and price data files.
    '''
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)


    report = make_report_data(portfolio, prices)


    formatter = tableformat.create_formatter(fmt)
    print_report(report,formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2],args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
    


