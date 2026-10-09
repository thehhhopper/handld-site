# handld Trading Risk Disclosure

Version: to be confirmed. Last updated: 9 Oct 2026.

Read this before you connect your Hyperliquid account or send a trade. It is part of the handld [Terms of Use](/terms). It does not list every risk.

Contact: {{LEGAL_CONTACT_EMAIL}}.

## The short version

- **You can lose all the money in your Hyperliquid account.** Losses can happen fast.
- handld does not choose your trades and does not give advice. You pick the symbol, the direction and the invalidation.
- **You will not see the size or the stop in the desk.** A placed trade and a refused trade generally both read "Handled." Check your positions in your own Hyperliquid account.
- A stop is an order, not a promise. It may fill far from its price, or not at all.
- Only trade with money you can afford to lose entirely.

## 1. Perpetual futures

Perpetual futures ("perps") are derivatives. They let you take a position on the price of a crypto asset without owning it, with no expiry date. Crypto prices can move very sharply, at any hour, including weekends. Perps are complex and high risk and are not suitable for everyone.

## 2. Leverage

Perps on Hyperliquid are traded with leverage. Leverage means a small price move produces a much larger gain or loss relative to the margin in your account. The size the desk calculates under the Ruleset determines how much of your account is exposed on each trade, and you will not see it in the desk.

## 3. Liquidation

If losses reduce your margin below Hyperliquid's maintenance requirement, Hyperliquid can liquidate your position automatically, in whole or part, possibly before any stop fills. Liquidation is run by Hyperliquid, not handld. You can lose your margin, and liquidation can come with extra fees.

## 4. Gaps, slippage and stops

- A stop is an order placed on Hyperliquid. **It is not a promise of any exit price.** In fast or thin markets the price can jump past your stop ("gap"), and the fill can be much worse than the stop price ("slippage").
- A stop can also fail to be placed, updated or triggered because of venue outages, rejected orders, rate limits, network problems, or a fault at handld.
- **Stop versus invalidation.** Your invalidation is the price where you consider your idea wrong. Under the Ruleset the stop may sit **further** from entry than your invalidation. It is never placed closer. So the price can pass your invalidation and keep going before the stop is reached. The stop does not hold your loss at your invalidation, or at any fixed amount.

## 5. Funding

Perps charge or pay **funding** at regular intervals, depending on the gap between the perp price and the underlying price. Funding can work against you every interval while your position is open, and can add up over time. Funding is set by Hyperliquid and is separate from handld's fees.

## 6. Hyperliquid venue risk

Your account and positions live on Hyperliquid, an independent third party that handld does not control. Risks include:

- **Venue risk:** outages, halts, changes to its rules, margin or listing decisions, delistings, or Hyperliquid restricting or closing your account.
- **Smart-contract and protocol risk:** bugs, exploits or failures in Hyperliquid's chain, bridge or contracts, which could cause loss of funds.
- **Oracle and pricing risk:** wrong or manipulated price feeds can trigger liquidations or stops at prices that do not reflect the wider market.
- **Network risk:** congestion, validator issues, or failures in the internet, wallets or browsers between you, handld and Hyperliquid.

Hyperliquid states in its own terms that it is not licensed in any jurisdiction. Read Hyperliquid's terms at https://app.hyperliquid.xyz/terms.

## 7. Agent-key risk

You authorise a trade-only agent (API) key so the desk can place and cancel orders. It cannot withdraw funds. But if that key is misused or compromised, whether at handld or on your side, someone could place or cancel orders on your account, including large or unwanted ones. You can revoke the key on Hyperliquid at any time. Revoking it stops the desk acting, but does **not** close your open positions or cancel your open orders. You must manage those in Hyperliquid. Never share your master private key or seed phrase with anyone.

## 8. The desk is opaque. Understand this before you accept.

- When you send a trade, you instruct handld to apply the Ruleset you accepted, at the size and stop it calculates, **without showing you those figures first**.
- The desk does not show size, stop, notional, leverage or the result of a trade. A placed trade and a trade refused under the Ruleset both read **"Handled."** You will not be told in the desk which happened or which rule applied. Only some refusals show a plain message instead: input errors, market-data problems, setup, account or connection problems, close failures, and location or eligibility checks (the categories are set out in [Schedule 1](/legal/refusals) of the Terms, section 5.5(b)). Every other refusal reads "Handled.".
- handld's operator tools and audit log do record size, stop, the allow or refuse reason and the Ruleset version.
- **You can see your actual positions, orders, fills, fees and balance in your own Hyperliquid account at any time.** Check it. If you do not, you may not realise a trade was placed, what size it is, or where its stop sits.
- Because you cannot see the figures in the desk, a mistake in your inputs, or a fault in handld, may not be obvious to you until you check Hyperliquid.

## 9. A refusal is not advice

If the desk refuses a trade, that is a rule in the Ruleset operating mechanically (for example a lockout or limit). It says nothing about whether the trade idea is good or bad. A trade the desk places is not an endorsement either. Lockouts can also stop you entering or re-entering a trade you wanted, including one that would have moved your way. After a bad month under the Ruleset, risk is held at the lowest level until month end. That is not a lockout: trades still go through the Ruleset as usual, at the lowest risk level.

If your location cannot be confirmed because the location check is unavailable, the desk will not send new trades and shows "We can't confirm your location right now. Try again later." You may be unable to open a trade during that time.

## 10. Beta software

This is an early, invite-only cohort on mainnet with real funds. The software may have bugs, behave unexpectedly, be interrupted, or change. Results from testnet or paper trading do not predict mainnet results.

## 11. You can lose everything

Total loss of the funds in your Hyperliquid account is possible. Past results, yours or anyone's, do not predict future results. handld makes no promise of any return.

## 12. No regulatory protection or compensation scheme may apply

handld's regulatory status is to be confirmed. You should assume that **no investor-compensation scheme, deposit-insurance scheme, or financial ombudsman protection applies** to your use of handld or to your Hyperliquid account, and that you may not have the protections you would have with a licensed broker or investment firm.

## 13. Fees and costs

handld charges a 0.01% Hyperliquid builder fee on fills of orders the desk places. Hyperliquid charges its own trading fees, and funding applies (section 5). Costs add up and reduce your account balance whether trades win or lose. There is no subscription charge during this cohort. Subscription terms will be added before any charge.

## 14. Tax

You are solely responsible for working out, reporting and paying any tax on your trading, funding and fees in every country where you owe tax. handld does not give tax advice and does not withhold tax for you.

## 15. Legality where you are

Being on handld's launch allowlist does not mean crypto derivatives, or this Service, are permitted or suitable in your country. You are responsible for following the law that applies to you.

## Acknowledgement

I have read the Risk Disclosure. I understand that I can lose all the funds in my Hyperliquid account, that the stop may sit further than my invalidation and may not fill at its price, that size and stop are calculated under the Ruleset and not shown to me in the desk, that "Handled." does not tell me whether a trade was placed or refused, and that I can check my positions in my own Hyperliquid account.
