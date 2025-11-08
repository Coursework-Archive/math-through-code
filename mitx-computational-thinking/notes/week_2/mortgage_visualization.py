from __future__ import division
from matplotlib import pyplot as plt, legend
import numpy as np
import matplotlib.ticker as mtick

def find_payment(loan, annual_rate, months):
    """
    Compute the fixed monthly payment for an amortized loan.

    loan: principal (float)
    annual_rate: annual interest rate as a decimal (e.g., 0.05 for 5%)
    months: number of monthly payments (int)
    returns: monthly payment (float)
    """
    monthly_rate = annual_rate / 12.0
    # Handle the edge case of a 0% rate
    if monthly_rate == 0:
        return loan /float(months)
    return loan * ((monthly_rate * (1 + monthly_rate) ** months) /
                   ((1 + monthly_rate) ** months - 1))

def compare_mortgages(amt, years, fixed_rate, pts, pts_rate, var_rate1, var_rate2, var_months):
    tot_months = years * 12
    fixed1 = Fixed(amt, fixed_rate, tot_months)
    fixed2 = Fixed_with_pts(amt, pts_rate, tot_months, pts)
    two_rate = Two_rate(amt, var_rate2, tot_months, var_rate1, var_months)
    morts = [fixed1, fixed2, two_rate]
    for _ in range(tot_months):
        for mort in morts:
            mort.make_payment()

    plot_mortgages(morts, amt)

def plot_mortgages(morts, amt):
    def label_plot(figure, title, x_label, y_label):
        plt.figure(figure)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(loc = 'best')
    styles = ['k-', 'k-.', 'k:']
    payments, cost, balance, net_cost = 0, 1, 2, 3 # figure numbers
    for i, mort in enumerate(morts):
        plt.figure(payments); mort.plot_payments(styles[i])
        plt.figure(cost); mort.plot_tot_pd(styles[i])
        plt.figure(balance); mort.plot_balance(styles[i])
        plt.figure(net_cost); mort.plot_net(styles[i])

    label_plot(payments, 'Monthly Payments of {:,} Mortgages'.format(amt), 'Months', 'Monthly Payments ($)'); _prettify_current_axes()
    label_plot(cost, 'Cash Outlay of {:,} Mortgages'.format(amt), 'Months', 'Total Payments ($)'); _prettify_current_axes()
    label_plot(balance, 'Balance Remaining of {:,} Mortgages'.format(amt), 'Months', 'Remaining Balance ($)'); _prettify_current_axes()
    label_plot(net_cost, 'Net Cost of {:,} Mortgages'.format(amt), 'Months', 'Payments - Equity ($)' ); _prettify_current_axes()

def _prettify_current_axes():
    ax = plt.gca()
    ax.grid(True, alpha=0.3)
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

class Mortgage(object):
    """abstract class for building different kinds of mortgages"""
    def __init__(self, loan, annRate, months, legend=None):
        self._loan = float(loan)
        self._rate = float(annRate) / 12.0
        self._months = int(months)
        self._paid = [0.0]              # amount paid each month (0.0 before any payment)
        self._outstanding = [self._loan] # remaining balance (starts at loan)
        self._payment = find_payment(self._loan, annRate, self._months)
        # description used in legends; fall back to a simple label
        self._legend = (legend if legend is not None
                        else "Loan ${:,.0f} @ {:.2f}% for {} mo".format(
                    self._loan, annRate * 100.0, self._months))

    def make_payment(self):
        """Record one month of payment and update remaining balance."""
        self._paid.append(self._payment)
        # interest portion this month
        interest = self._outstanding[-1] * self._rate
        # reduction of principal this month
        reduction = self._payment - interest
        self._outstanding.append(self._outstanding[-1] - reduction)

    def get_total_paid(self):
        return sum(self._paid)

    def __str__(self):
        return self._legend

    # ---------------- Plot helpers (match the book) -----------------
    def plot_payments(self, style):
        # skip the initial 0.0 placeholder
        plt.plot(self._paid[1:], style, label=self._legend)

    def plot_balance(self, style):
        plt.plot(self._outstanding, style, label=self._legend)

    def plot_tot_pd(self, style):
        # cumulative sum of payments
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])
        plt.plot(tot_pd, style, label=self._legend)

    def plot_net(self, style):
        # total paid so far
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])

        # equity acquired = original loan minus current outstanding
        equity_acquired = (np.array([self._loan] * len(self._outstanding))
                            - np.array(self._outstanding))
        net = np.array(tot_pd) - equity_acquired
        plt.plot(net, style, label=self._legend)


    @property
    def months(self):
        return self._months

class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self._legend = 'Fixed, {:.1f}%'.format(r * 100)

class Fixed_with_pts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self._pts = pts
        self._paid = [loan * (pts / 100)]
        self._legend = ('Fixed, {:.1f}% {} points'.format( r * 100, pts))

class Two_rate(Mortgage):
    def __init__(self, loan, r, months, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self._teaser_months = teaser_months
        self._next_rate = float(r) / 12.0
        self._legend = ('{:.1f}% for {} months, then {:.1f}%'
                        .format(100 * teaser_rate,
                                self._teaser_months,
                                100 * r))

    def make_payment(self):
        if len(self._paid) == self._teaser_months + 1:
            self._rate = self._next_rate
            self._payment = find_payment(
                self._outstanding[-1],
                self._rate * 12,
                self._months - self._teaser_months
            )

        Mortgage.make_payment(self)

# ---------------- Demo ------------------
if __name__ == "__main__":
    # Example 1: Single mortgage demo
    # Example: $850k, 5% APR, 30-year (360 months)
    # m = Mortgage(loan=850000, annRate=0.05, months=360,
    #              legend="Loan $100,000 @5.00% for 30 yrs")
    #
    # # simulate full term
    # for _ in range(m.months):
    #     m.make_payment()
    #
    # #Figure 1: monthly payment series
    # plt.figure(1)
    # m.plot_payments('b-')
    # plt.title('Monthly Payments')
    # plt.xlabel('Month')
    # plt.ylabel('Payment ($)')
    # plt.legend()
    #
    # # Figure 2: remaining balance
    # plt.figure(2)
    # m.plot_balance('r-')
    # plt.title('Outstanding Balance')
    # plt.xlabel('Month')
    # plt.ylabel('Balance ($)')
    # plt.legend()
    #
    # # Figure 3: total paid (cumulative)
    # plt.figure(3)
    # m.plot_net('g--')
    # plt.title('Total Paid Over Time')
    # plt.xlabel('Month')
    # plt.ylabel('Net Dollars ($)')
    # plt.legend()
    #
    # # Figure 4: net cost (total paid minus equity acquired)
    # plt.figure(4)
    # m.plot_net('k-.')
    # plt.title('Net Cost of Mortgage Over Time')
    # plt.xlabel('Month')
    # plt.ylabel('Net Dollars ($)')
    # plt.legend()

    # ---- Example 2: Compare several mortgages (from the book) ----
    compare_mortgages(
        amt=650000,          # principal
        years=30,            # 30-year term
        fixed_rate=0.07,     # 7%
        pts=3.25,            # points for the second mortgage
        pts_rate=0.065,      # 6.5% with points
        var_rate1=0.045,     # 4.5% teaser
        var_rate2=0.075,     # 7.5% after teaser
        var_months=48        # 4 years teaser period
    )

    plt.show()
