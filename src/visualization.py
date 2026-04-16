import matplotlib.pyplot as plt
import seaborn as sns

def plot_performance(data):
    (data / data.iloc[0]).plot(figsize=(10,6))
    plt.title("Stock Performance Over Time")
    plt.show()

def plot_correlation(corr):
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

def plot_risk_return(risk, mean_return):
    plt.scatter(risk, mean_return)

    for i in risk.index:
        plt.text(risk[i], mean_return[i], i)

    plt.xlabel("Risk (Volatility)")
    plt.ylabel("Return")
    plt.title("Risk vs Return")
    plt.show()

def plot_efficient_frontier(results, best=None):
    returns = [r[0] for r in results]
    vol = [r[1] for r in results]
    sharpe = [r[2] for r in results]

    plt.scatter(vol, returns, c=sharpe)

    # ⭐ Highlight best portfolio
    if best:
        plt.scatter(best[1], best[0], color='red', s=100, label='Optimal Portfolio')
        plt.legend()

    plt.colorbar(label="Sharpe Ratio")
    plt.xlabel("Volatility")
    plt.ylabel("Return")
    plt.title("Efficient Frontier")
    plt.show()

def plot_interest_vs_returns(merged_data):
    import matplotlib.pyplot as plt

    for col in merged_data.columns:
        if col != "Interest_Rate":
            plt.scatter(merged_data["Interest_Rate"], merged_data[col], label=col)

    plt.xlabel("Interest Rate")
    plt.ylabel("Stock Returns")
    plt.title("Interest Rate vs Stock Returns")
    plt.legend()
    plt.show()