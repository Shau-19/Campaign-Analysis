# **Marketing Campaign Performance Analysis **  

## **Project Overview**  
This project analyzes the performance of **1,000 marketing campaigns** across different **channels, product categories, and promotion types**. The goal is to evaluate key performance metrics, identify successful strategies, and optimize future marketing investments.  

### **Dataset Description**  
The dataset (`dataset_sales.csv`) contains the following fields:  
- **Campaign_ID**: Unique identifier for each campaign  
- **Campaign_Name**: Name of the campaign  
- **Product_Category**: Type of product (Sneakers, Apparel, Accessories)  
- **Channel**: Marketing channel (Facebook, Instagram, Email, YouTube, TikTok, Google Ads)  
- **Promo_Type**: Type of promotion (Seasonal Sale, Flash Sale, New Launch, Influencer Collab, Limited Edition)  
- **Impressions**: Number of times the ad was displayed  
- **Clicks**: Number of clicks on the ad  
- **Conversions**: Number of completed purchases/sign-ups  
- **Cost**: Total cost of the campaign  
- **Revenue**: Total revenue generated  

---

## **Key Performance Metrics Evaluated**  

### **1. Engagement Metrics**  
- **Click-Through Rate (CTR)**  
  - Measures ad engagement  
  - Formula:  
    \[
    CTR = \left( \frac{\text{Clicks}}{\text{Impressions}} \right) \times 100
    \]  

- **Conversion Rate**  
  - Measures effectiveness in driving actions  
  - Formula:  
    \[
    \text{Conversion Rate} = \left( \frac{\text{Conversions}}{\text{Clicks}} \right) \times 100
    \]  

### **2. Financial Metrics**  
- **Return on Investment (ROI)**  
  - Measures profitability  
  - Formula:  
    \[
    ROI = \left( \frac{\text{Revenue} - \text{Cost}}{\text{Cost}} \right) \times 100
    \]  

- **Cost Per Click (CPC)**  
  - Measures cost efficiency per engagement  
  - Formula:  
    \[
    CPC = \frac{\text{Cost}}{\text{Clicks}}
    \]  

- **Cost Per Conversion**  
  - Measures cost efficiency per sale  
  - Formula:  
    \[
    \text{Cost Per Conversion} = \frac{\text{Cost}}{\text{Conversions}}
    \]  

- **Revenue Per Conversion**  
  - Measures average revenue per sale  
  - Formula:  
    \[
    \text{Revenue Per Conversion} = \frac{\text{Revenue}}{\text{Conversions}}
    \]  

---

## **Analysis Approach**  

### **1. Channel Performance Comparison**  
- Which marketing channels (Facebook, Instagram, Email, etc.) have the highest **CTR, conversion rate, and ROI**?  
- Which channels are most cost-effective for driving conversions?  

### **2. Product Category Analysis**  
- Which product categories (**Sneakers, Apparel, Accessories**) perform best in terms of engagement and profitability?  
- Are certain categories more effective on specific channels?  

### **3. Promotion Type Effectiveness**  
- Which **promo types** (Seasonal Sale, Flash Sale, New Launch, etc.) generate the highest ROI?  
- Do certain promotions work better for specific product categories?  

### **4. Top-Performing Campaigns**  
- Identify campaigns with the **highest ROI, conversion rates, and revenue**.  
- Analyze what made them successful (channel, promotion type, product category).  

### **5. Budget Optimization Recommendations**  
- Based on findings, suggest **optimal budget allocation** for future campaigns.  

---

## **Key Findings & Insights**  
*(Summary of major trends and takeaways from the analysis)*  

1. **Best Performing Channel:** [Channel with highest ROI]  
2. **Most Engaging Promotion Type:** [Promo type with highest CTR]  
3. **Highest Converting Product Category:** [Category with best conversion rate]  
4. **Most Cost-Efficient Campaigns:** [Campaigns with lowest CPC & highest ROI]  

---

## **Recommendations for Future Campaigns**  
1. **Increase investment in [Top Channel]** due to high ROI.  
2. **Use [Best Promo Type] more frequently** for better engagement.  
3. **Optimize budget allocation** by reducing spend on underperforming channels.  
4. **Test new strategies** for low-performing categories (e.g., influencer collaborations for Accessories).  

---

## **Files Included**  
1. **`dataset_sales.csv`** – Raw dataset of 1,000 marketing campaigns  
2. **`campaign_analysis.ipynb`** (or `.py`) – Code for data cleaning, analysis, and visualization  
3. **`visualizations/`** – Charts & graphs (e.g., CTR by channel, ROI by promo type)  and SQL analysis


---

## **How to Reproduce the Analysis**  
1. **Run the Jupyter Notebook/Python script** to process the data.  
2. **Review visualizations** for insights.  
3. **Adjust parameters** (e.g., filter by date, category) for deeper analysis.  

---

## **Dashboard**
Here are link which can be followed for better visualization of data 
**Dashboard link**:- https://campaign-analysis-final.onrender.com/
**EDA Report**:- https://shau-19.github.io/Campaign-Analysis/index.html#sample



