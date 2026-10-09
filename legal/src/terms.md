# handld Terms of Use

Version: to be confirmed. Effective date: to be confirmed. Last updated: 9 Oct 2026.

## 1. Who we are and what these Terms cover

1.1 These Terms of Use ("Terms") are an agreement between you and handld (company in formation) ("handld", "we", "us").

1.2 These Terms apply to the handld website (handld.xyz), the web desk at app.handld.xyz, and any related software, support and communications (together, the "Service").

1.3 By accepting these Terms in the onboarding flow you confirm that you have read and accept them, the [Risk Disclosure](/risk), the [Privacy Notice](/privacy), and the Ruleset version shown to you at acceptance. If you do not accept, do not use the Service.

1.4 Contact: {{LEGAL_CONTACT_EMAIL}}.

## 2. What handld is, and what it is not

2.1 handld is an execution-and-constraint desk. It is software that, on your instruction, places, updates and cancels orders on your own Hyperliquid account, only as a published Ruleset you have accepted specifies.

2.2 For each trade you supply three things: the **symbol**, the **direction**, and an **invalidation level** (the price at which you consider your trade idea wrong). Under the Ruleset, the desk then calculates the position size and the stop. The desk may also **refuse** a trade, for example because a lockout, limit or other rule in the Ruleset applies.

2.3 handld is **not**:

- investment advice, a personal recommendation, or tailored advice of any kind;
- discretionary portfolio management. We do not choose your instrument, your direction, or when you trade, and we exercise no judgment outside the Ruleset;
- a signals, alerts or strategy service;
- a broker, exchange, venue, bank, custodian or insurer.

2.4 You alone choose each trade idea and decide whether to send it. Choosing a Ruleset is your choice of pre-published constraints. It does not appoint us to manage your account or your positions.

## 3. Eligibility

3.1 The Service is available **by invitation only**. An invitation is personal to you and cannot be transferred, shared or sold.

3.2 To use the Service you must, at all times:

- (a) be at least **18 years old** and have full legal capacity to enter into these Terms;
- (b) be both **resident in** and **physically located in** a country on our current launch allowlist, as shown in the onboarding flow (to be confirmed). The allowlist can change. A country being on it does not mean that crypto derivatives, or this Service, are permitted or suitable where you live;
- (c) **not** be a US person, and not be resident in, located in, or (for an entity) incorporated in or registered in the United States;
- (d) **not** be resident in or located in the Province of Ontario, Canada;
- (e) **not** be a resident or a citizen of, or located in, any comprehensively sanctioned country or region. This currently includes Cuba, Iran, North Korea, Syria, Russia, Belarus, Venezuela, Myanmar, Sudan, South Sudan, and the Crimea, Donetsk and Luhansk regions of Ukraine. We may add to this list at any time;
- (f) **not** be, or act for or on behalf of, any person or entity named on, or owned or controlled by a person named on, a sanctions list maintained by the United Nations, the European Union, the United Kingdom or the United States, or otherwise subject to sanctions;
- (g) **declare every nationality you hold**, truthfully and completely. If any one of them is on the refused list in 3.2(e), you are not eligible, whatever your other nationalities or your country of residence;
- (h) **not** use a VPN, proxy, anonymising network, or any other means to mask, spoof or misstate your location or identity;
- (i) comply with Hyperliquid's own terms of use (https://app.hyperliquid.xyz/terms) and be eligible to use Hyperliquid yourself;
- (j) be permitted under the laws that apply to you to use the Service and to trade crypto perpetual futures.

3.3 You must tell us promptly at {{LEGAL_CONTACT_EMAIL}} if any of the facts in 3.2 change, including if you move country or acquire a new nationality.

3.4 We check eligibility using what you declare and technical signals (for example IP-based location, and later card billing country). We may ask for more information. We may refuse an invitation, refuse a signup, block an order or a session, suspend or end your access for any eligibility, location, sanctions or legal reason, without saying which check applied.

## 4. Your account and access

4.1 You must give accurate information and keep it up to date. You are responsible for all activity under your account and for keeping your login and devices secure.

4.2 One person, one account. Do not let anyone else use your account or your invitation.

4.3 We may limit the number of accounts, symbols, concurrent positions or other features available to the cohort.

## 5. How the desk works (opaque Ruleset)

5.1 **The Ruleset.** Before you can send a trade you must actively accept a published, versioned Ruleset (for example `handld-poc-v1`). The Ruleset sets out how position size is calculated, when the stop may sit further from entry than your invalidation, and the lockouts and breakers that apply. You can review the full Ruleset at any time in Settings.

5.2 **Your instruction.** Sending a trade through the desk is your instruction to handld to apply the Ruleset you accepted to your symbol, direction and invalidation, and to place, update and cancel orders on your Hyperliquid account at the size and stop the Ruleset calculates, **without first showing you those figures**.

5.3 **Size and stop are calculated, not chosen by you, and not shown to you in the desk.** Position size and stop placement are calculated solely by applying the published Ruleset you selected to your symbol, direction and invalidation. Risk per trade is not a setting you control. It follows from the Ruleset (including ladder progress and stop distance).

5.4 **Stop versus invalidation.** Your invalidation is the thesis boundary you chose. The stop is the order the Ruleset places on the venue. Under the Ruleset the stop **may sit further from entry than your invalidation. It will never be placed closer.** A stop is an order, not an outcome. It does not limit your loss to any amount and may not fill at or near its price (see the Risk Disclosure).

5.5 **Opacity: what you will and will not see.** Please read this carefully.

- (a) The desk does **not** show you the position size, the stop price, the notional, the leverage, or the gain or loss on a trade.
- (b) **When "Handled." appears, and when it does not.** When the desk is up and your trade phrase is valid, a trade the desk places and a trade the Ruleset refuses both read **"Handled."** You will not be told in the desk whether the trade was placed or refused, or which rule applied. A completed close also reads "Handled." Some refusals are instead shown with a plain message and never with "Handled.". These fall into the following categories:
- (i) **input errors**: the trade phrase can't be read, or the invalidation is on the wrong side of the market or otherwise unusable (for example an unsupported timeframe or distance), or an entry type the desk does not offer, such as a limit entry;
- (ii) **market-data problems**: the symbol is not on the venue, venue inventory is unavailable, or the market price or candle data is missing or out of date;
- (iii) **setup, account and connection problems**: setup is not finished, the wallet, agent key, builder-fee approval or sign-in is missing or revoked, the desk is offline, not connected or busy, the desk could not complete a call or check your limits, the desk is checking your positions, or your Hyperliquid account changed outside the desk;
- (iv) **close failures**: a close did not complete, or completed only in part;
- (v) **location and eligibility checks**: handld is not available in your country or current location, a VPN or proxy is suspected, or your residence and nationality declaration is missing. If your location cannot be confirmed because the location check itself is unavailable, the desk does not proceed and shows "We can't confirm your location right now. Try again later." (for orders, preceded by "Not sent."); and
- (vi) **setup and acceptance screens**, for example when the Ruleset changed since the page loaded.

These categories are set out in [Schedule 1](/legal/refusals), and may be updated as the product changes. **Every other refusal reads "Handled."** None of these messages shows size, stop, leverage, gains or losses, or the name of the rule that applied.

- (c) handld's operator tools and audit log **do** record, for every trade, your inputs, the calculated size and stop (including whether the stop sits further than your invalidation), the allow or refuse reason, the Ruleset version and timestamps.
- (d) **You can always see your actual positions, open orders, fills, fees and balances directly in your own Hyperliquid account**, outside handld.

5.6 **Refusals are not advice.** If the desk refuses a trade, that is the Ruleset's mechanical constraint operating. It is not a view, opinion or recommendation on the trade, the market or you. A trade the desk places is equally not an endorsement.

5.7 **Lockouts, breakers and the bad-month rule.** The Ruleset may stop you opening new trades for a period (for example after daily or weekly loss limits). Lockouts are enforced on our servers. Restarting the app or signing out does not clear them. Separately, if losses in a calendar month reach the Ruleset's monthly loss level (the bad-month rule), **risk is held at the lowest level until month end (UTC).** You can still send trades, and the Ruleset still places or refuses them as usual, but size is calculated at the lowest risk level until the month ends. From the next month, risk returns to the level reached under the Ruleset before the bad month. This is not a lockout. Daily, weekly and monthly limits use UTC. A day runs 00:00 to 00:00 UTC, a week runs from Monday 00:00 UTC, and a month is the UTC calendar month. Lockouts end at the next UTC boundary, and the bad-month rule ends at 00:00 UTC on the 1st.

5.8 **Open positions.** Open positions follow the Ruleset version disclosed for them. The desk places, updates and cancels bracket orders only as the Ruleset specifies.

5.9 **Testnet and paper.** Any paper or testnet mode is for practice only and has no effect on your mainnet account.

## 6. Ruleset changes

6.1 We may publish new Ruleset versions. Ruleset text and version history stay reviewable in the product.

6.2 Changes you make within the product: tightening takes effect at once. Loosening is queued for seven days, and the old rule stays live until then.

6.3 If we change the Ruleset in a way that materially affects how size, stops, lockouts or refusals work, we will tell you by a method to be confirmed, at least a period to be confirmed before it applies, and ask you to re-accept before your next trade.

## 7. Your funds, your Hyperliquid account and the agent key (non-custodial)

7.1 **We never hold your funds.** Your funds stay in your own Hyperliquid account at all times. handld does not take custody of, hold, pool or move your assets.

7.2 **Trade-only agent key.** To connect, you authorise a Hyperliquid agent (API) wallet for handld from your own wallet. That key can place and cancel orders on your account. It **cannot withdraw** funds. handld never asks for, receives or stores your master private key or seed phrase. Never give them to anyone, including anyone claiming to be handld.

7.3 **You can revoke the agent key on Hyperliquid at any time.** Once you revoke it the desk can no longer place, update or cancel orders for you. **Revoking does not by itself close your positions or cancel your open orders on Hyperliquid.** Any open position, stop or other order may stay live until you manage it in Hyperliquid.

7.4 **Transfers are yours.** Moving funds between spot and perpetuals, deposits and withdrawals are your own actions in the Hyperliquid interface. The desk will not move funds for you.

7.5 **Agent-key risk.** A trade-only key, if misused or compromised (at our side or yours), could place or cancel orders, including orders you did not intend. If you suspect misuse, revoke the key on Hyperliquid immediately and tell us at {{LEGAL_CONTACT_EMAIL}}.

7.6 Hyperliquid is an independent third party. We do not control it and are not responsible for its availability, rules, liquidations, pricing, fees or any loss arising from it. Your use of Hyperliquid is governed by its own terms.

## 8. Fees

8.1 **Builder fee.** On fills of orders the desk places for you, a Hyperliquid builder fee of **0.01%** is charged. The fee base is to be confirmed. You approve the builder fee from your own wallet on Hyperliquid before the desk can trade. Hyperliquid's own trading fees and funding payments are separate and are set by Hyperliquid.

8.2 **Subscriptions are not live.** There are no paid seats yet and we will not charge any subscription during this cohort without your separate agreement. Before any subscription is charged, we will add subscription terms (price, billing period, renewal, cancellation, refunds, taxes and any withdrawal or cooling-off rights) and ask you to accept them.

8.3 **No performance-based fees.** No fee we charge depends on whether your trades gain or lose. We never take a share of gains.

8.4 You are responsible for all taxes on your trading and on your use of the Service.

## 9. Points and promotions

9.1 Any points, loyalty, referral or rewards programme will be governed by its own separate terms, published before it starts. Nothing in these Terms gives you any right to points, rewards, or any cash or token value.

## 10. Beta cohort; Service provided "as is"

10.1 This is an early, invite-only mainnet cohort. The Service is in beta. It may contain errors, change without notice, be interrupted, or be withdrawn.

10.2 The Service is provided **"as is" and "as available"**. To the fullest extent permitted by law, we make no warranty or representation that the Service will be uninterrupted, timely, error-free or fit for any particular purpose, that orders will be placed, updated or cancelled when or as intended, or that any outcome will follow from using it.

10.3 Real funds are at risk on mainnet. Use only funds you can afford to lose entirely.

## 11. Risk

11.1 Trading crypto perpetual futures with leverage is high risk. **You can lose some or all of the funds in your Hyperliquid account.** The [Risk Disclosure](/risk) forms part of these Terms. Read it before you trade.

11.2 We make no representation about future results. Nothing in the Service is a promise of any return.

## 12. Acceptable use

You must not:

- (a) misstate your identity, age, residence, location or nationality, or use a VPN, proxy or other location masking;
- (b) use the Service in breach of any sanctions, export-control, anti-money-laundering or other law, or for anyone else's benefit;
- (c) share, sell or transfer your invitation or account;
- (d) probe, scan, reverse engineer, overload or interfere with the Service, or try to extract the size, stop or refusal logic through the desk;
- (e) use the Service to manipulate any market or breach Hyperliquid's terms;
- (f) access the Service by automated means other than those we provide.

## 13. Suspension and termination

13.1 You may stop using the Service at any time by revoking the agent key on Hyperliquid and contacting {{LEGAL_CONTACT_EMAIL}} (closing the account in the product is to be confirmed).

13.2 We may suspend or end your access at any time, with or without notice, including if we believe you are not eligible, have breached these Terms, pose a legal, sanctions or security risk, or if we close the cohort or the Service.

13.3 When access ends, the desk stops placing, updating and cancelling orders and stops enforcing the Ruleset for you. It does not by itself close your positions or cancel open orders on Hyperliquid. You are responsible for managing them there.

13.4 Sections 7.6, 8.4, 10, 11, 16, 17, 19 and 20 survive termination, as do any fees owed.

## 14. Third-party services

The Service depends on third parties, including Hyperliquid (the venue) and, once paid seats exist, Stripe (payments), together with hosting, email and other providers listed in the Privacy Notice. Their services are governed by their own terms. We are not responsible for their acts, failures or outages.

## 15. Intellectual property and feedback

We (or our licensors) own the Service, the Ruleset and all related software and content. We grant you a personal, revocable, non-transferable licence to use the Service under these Terms during your access. If you send us feedback, we may use it freely.

## 16. Limitation of liability

16.1 To the fullest extent permitted by applicable mandatory law, handld is not liable for:

- trading losses, liquidations, missed, late or partial fills, slippage, or gaps;
- outcomes of the Ruleset applied as published and accepted by you, including refusals and lockouts;
- Hyperliquid or other third-party outages, errors, rule changes or failures, including smart-contract, oracle or network failures;
- loss of opportunity, revenue or data, or any indirect or consequential loss.

16.2 Our total liability to you under or in connection with these Terms is limited to an amount to be confirmed.

16.3 Nothing in these Terms limits or excludes liability that cannot lawfully be limited or excluded, including for fraud, intent or gross negligence, death or personal injury caused by negligence, or mandatory consumer rights.

## 17. Privacy

We process your personal data as described in the [Privacy Notice](/privacy), including for eligibility and sanctions checks and to keep the audit log described in 5.5(c).

## 18. Changes to these Terms

We may change these Terms. For material changes we will give you notice to be confirmed before they apply and, where required, ask you to re-accept. If you do not accept a change, stop using the Service and revoke the agent key.

## 19. Governing law and disputes

19.1 These Terms are governed by laws to be confirmed, without prejudice to mandatory consumer protections of the country where you live that cannot be waived.

19.2 Forum: to be confirmed. If you are an EEA consumer, nothing here removes your right to bring proceedings in the courts of your Member State where the law gives you that right.

## 20. Complaints and contact

Complaints and legal notices: {{LEGAL_CONTACT_EMAIL}}. We aim to acknowledge complaints within a period to be confirmed and respond within a period to be confirmed.

## 21. General

21.1 If any part of these Terms is unenforceable, the rest stays in effect. 21.2 Our not enforcing a right is not a waiver. 21.3 You may not transfer these Terms. We may transfer them to an affiliate or a successor. 21.4 These Terms, the Risk Disclosure, the Privacy Notice, the accepted Ruleset and any separate programme or subscription terms are the whole agreement between us about the Service. 21.5 Language: English (translation requirements are to be confirmed).
