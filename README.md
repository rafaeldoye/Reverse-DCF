# **Reverse Discounted Cash Flow (DCF) Analysis**

This Python program performs a Reverse Discounted Cash Flow (DCF) analysis to determine the **implied growth rate** priced into a stock. Additionally, it calculates the intrinsic value of a company based on the given parameters and compares it to the current market price.

---

## **Features**

- **Implied Growth Rate Calculation**: Reverse-engineers the Free Cash Flow (FCF) growth rate assumed by the current stock price.
- **Intrinsic Value Estimation**: Computes the intrinsic value of the company and the intrinsic value per share.
- **Upside/Downside Analysis**: Quantifies the percentage difference between the intrinsic value per share and the current stock price.
- **User-Friendly Inputs**: Prompts for key financial metrics to perform the analysis.

---

## **How It Works**

1. **User Inputs**:
   - Initial Free Cash Flow (FCF) in millions.
   - Discount rate (as a decimal, e.g., `0.10` for 10%).
   - Number of projection years.
   - Terminal growth rate (as a decimal, e.g., `0.03` for 3%).
   - Number of shares outstanding (in millions).
   - Current stock price per share (in dollars).

2. **Reverse DCF Logic**:
   - **Present Value of Cash Flows**:
     Calculates the present value of projected future FCFs and the terminal value.
   - **Implied Growth Rate**:
     Uses a binary search method to find the growth rate that matches the company's market capitalization (current stock price × number of shares outstanding).
   - **Intrinsic Value**:
     Computes the intrinsic value of the company using the implied growth rate.

3. **Output**:
   - Implied growth rate (from reverse DCF).
   - Intrinsic value of the company (in millions).
   - Intrinsic value per share.
   - Upside/downside percentage compared to the current stock price.

---

## **Requirements**

- Python 3.x
- Library:
  - `numpy`

Install the required library using pip:
```bash
pip install numpy
```

---

## **Usage**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/reverse-dcf.git
   cd reverse-dcf
   ```

2. **Run the Program**:
   ```bash
   python reverse_dcf.py
   ```

3. **Follow the Prompts**:
   - Enter the required inputs (initial FCF, discount rate, etc.) as prompted by the program.
   - View the results, including the implied growth rate, intrinsic value, and upside/downside.

---

## **Example Output**

### Input:
```plaintext
Enter the initial Free Cash Flow (FCF) in millions: 500
Enter the discount rate (as a decimal, e.g., 0.10 for 10%): 0.08
Enter the number of years for projection: 10
Enter the terminal growth rate (as a decimal, e.g., 0.03 for 3%): 0.03
Enter the number of shares outstanding (in millions): 50
Enter the current price per share (in dollars): 120
```

### Output:
```plaintext
--- Reverse DCF Analysis ---

Implied growth rate (from reverse DCF): 0.094563 (or 9.46%)

Intrinsic Value of the company: $5,500.32 million
Intrinsic Value per share: $110.01
Current price per share: $120.00
Upside/Downside: -8.33%

The company is currently priced assuming a growth rate of: 9.46%
```

---

## **File Structure**

```
reverse-dcf/
│
├── reverse_dcf.py        # Main Python script
├── README.md             # Documentation file
```
