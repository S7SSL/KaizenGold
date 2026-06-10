SLUG = "what-is-a-performance-bond-in-gold-trading"
TITLE = "What Is a Performance Bond in Gold Trading?"
CATEGORY = "Trade Finance"
DESC = "A performance bond is a bank-issued guarantee — commonly around 2% of contract value — that compensates the buyer if the seller fails to deliver gold as contracted. Learn how it works."
CARD = "The seller-side guarantee — typically ~2% of contract value — that backs the obligation to deliver."
ABOUT = ["Performance bond", "Bank guarantee", "Gold trading", "Trade finance"]
RELATED = ["dlc-vs-sblc-explained", "what-is-an-mt700-dlc", "what-is-a-cif-gold-transaction"]

LEAD = """<strong>A performance bond in gold trading is a bank-issued guarantee, typically for around 2% of the contract value, that compensates the buyer if the seller fails to deliver the gold as contracted.</strong> It is the seller-side counterpart to the buyer's letter of credit: the buyer's bank promises payment against documents, and the seller's bank promises a defined sum if the seller does not perform. Together the two instruments balance risk on both sides of a physical gold transaction."""

BODY = """
<h2>Why Performance Bonds Exist</h2>
<p>When a buyer opens a <a href="/knowledge/what-is-an-mt700-dlc/">documentary letter of credit</a>, it incurs real costs and ties up credit lines &mdash; before any gold has moved. If the seller then never ships, the buyer has spent money and reserved capital for nothing. The performance bond addresses this asymmetry: the seller's bank issues a guarantee in the buyer's favour, payable if the seller fails to deliver within the contract terms. It demonstrates the seller's seriousness and gives the buyer a defined remedy for non-performance.</p>

<h2>How It Works</h2>
<ol>
<li><strong>Contract terms.</strong> The sale contract specifies that the seller will provide a performance bond &mdash; commonly around 2% of contract value, though the percentage is negotiable &mdash; and defines the trigger for a claim (failure to ship by the latest shipment date, for example).</li>
<li><strong>Sequencing.</strong> Timing is heavily negotiated. A common structure: the buyer's bank issues the DLC, which becomes operative only when the seller's performance bond is in place; or the instruments are exchanged near-simultaneously through the banks.</li>
<li><strong>Issuance.</strong> The seller's bank issues the bond &mdash; in international practice usually as a demand guarantee (under the ICC's URDG 758) or as a <a href="/knowledge/dlc-vs-sblc-explained/">standby letter of credit</a>, transmitted bank-to-bank over SWIFT.</li>
<li><strong>Performance or claim.</strong> If the seller delivers, the bond expires undrawn. If the seller fails to perform, the buyer demands payment under the bond's terms and receives the guaranteed amount as compensation.</li>
</ol>

<h2>Example</h2>
<p>A buyer contracts for 100 kg of dor&eacute; delivered <a href="/knowledge/what-is-a-cif-gold-transaction/">CIF Dubai</a>, with a contract value at the agreed benchmark of, say, USD 10 million. The contract requires a 2% performance bond &mdash; USD 200,000. The buyer's bank issues the DLC; the seller's bank issues the performance bond; the DLC becomes operative. The seller ships on time, documents comply, the DLC pays, and the bond lapses unused. Had the seller missed the latest shipment date without excuse, the buyer would have claimed USD 200,000 under the bond to offset its costs.</p>

<h2>What a Performance Bond Is Not</h2>
<ul>
<li><strong>Not a payment instrument.</strong> It does not pay for gold; it compensates for non-delivery. Payment flows through the letter of credit.</li>
<li><strong>Not full contract cover.</strong> At ~2%, it covers the buyer's instrument costs and some losses &mdash; not the full value of an undelivered shipment.</li>
<li><strong>Not a substitute for due diligence.</strong> A bond from an unverifiable bank is worthless. As with all instruments in gold trading, authenticity is verified bank-to-bank over SWIFT.</li>
</ul>

<h2>Negotiating Points</h2>
<p>Sellers and buyers commonly negotiate: the percentage (and whether 2% is warranted for the deal size), the trigger events and documentation required to claim, the expiry date relative to the shipment schedule, which instrument form is used (demand guarantee vs standby), and the sequencing between bond issuance and DLC operativeness. Sequencing disputes &mdash; &ldquo;you first&rdquo; standoffs &mdash; are among the most common reasons otherwise-agreed gold transactions stall, which is why experienced facilitators define the exchange mechanics precisely in the contract.</p>
"""

TAKEAWAYS = [
    "A performance bond guarantees the seller's delivery obligation — commonly around 2% of contract value, payable to the buyer on non-performance.",
    "It mirrors the buyer's letter of credit: LC secures payment to the seller; the bond secures performance for the buyer.",
    "It is issued by the seller's bank, usually as a demand guarantee (URDG 758) or standby LC, transmitted over SWIFT.",
    "If the seller delivers as contracted, the bond expires undrawn; payment for the gold itself flows through the DLC.",
    "Sequencing between bond issuance and LC operativeness is a critical, heavily negotiated mechanic in gold contracts.",
]

FAQS = [
    ("Why is a performance bond usually 2%?",
     "Two percent is a long-standing commodity-trade convention that roughly matches the buyer's costs of opening the letter of credit. It is a convention, not a rule — the parties can agree any percentage."),
    ("Who issues the performance bond?",
     "The seller's bank, in favour of the buyer, against the seller's credit facilities. It is transmitted bank-to-bank over SWIFT (typically MT760 when issued as a guarantee or standby)."),
    ("When can the buyer claim under a performance bond?",
     "On the trigger events defined in the bond — typically the seller's failure to ship by the latest shipment date. Demand guarantees pay against a compliant written demand, so precise drafting of the trigger documentation matters."),
    ("Does the performance bond replace the letter of credit?",
     "No. They are complementary: the letter of credit pays the seller for delivered gold; the performance bond compensates the buyer if the gold is never delivered."),
    ("What happens to the bond after successful delivery?",
     "It expires automatically on its stated expiry date, undrawn, and the seller's bank releases the seller's facilities. Contracts often align expiry with the shipment schedule plus a margin."),
]
