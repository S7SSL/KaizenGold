SLUG = "what-is-lbma-pricing"
TITLE = "What Is LBMA Pricing?"
CATEGORY = "Pricing"
DESC = "The LBMA Gold Price is the global benchmark for gold, set twice daily in London via electronic auction and quoted in US dollars per troy ounce. Learn how it is set and used in contracts."
CARD = "The twice-daily London benchmark that international gold contracts price against — how it's set and applied."
ABOUT = ["LBMA", "LBMA Gold Price", "Gold pricing"]
RELATED = ["what-is-fine-gold-content", "what-is-a-cif-gold-transaction", "what-is-gold-dore"]

LEAD = """<strong>LBMA pricing refers to the LBMA Gold Price &mdash; the global benchmark price for gold, set twice each London business day (10:30am and 3:00pm London time) through an electronic auction administered by ICE Benchmark Administration, and quoted in US dollars per troy ounce of fine gold.</strong> International gold contracts, including dor&eacute; and bullion transactions, routinely fix their settlement price by reference to this benchmark."""

BODY = """
<h2>Who Sets the Price</h2>
<p>The <strong>London Bullion Market Association (LBMA)</strong> is the trade body at the centre of the world's largest over-the-counter gold market. The benchmark that bears its name, the LBMA Gold Price, is administered independently by <strong>ICE Benchmark Administration (IBA)</strong> as a regulated benchmark. Accredited participants &mdash; major bullion banks and trading houses &mdash; enter buy and sell orders into rounds of an electronic auction until the volume imbalance falls within tolerance; the final round's price becomes the benchmark for that session.</p>

<h2>Benchmark vs Spot</h2>
<p>Two prices are often confused:</p>
<table>
<tr><th></th><th>LBMA Gold Price (benchmark)</th><th>Spot price</th></tr>
<tr><td>When</td><td>Set twice daily (10:30 &amp; 15:00 London)</td><td>Continuous, around the clock on trading days</td></tr>
<tr><td>How</td><td>Auction among accredited participants</td><td>Streaming OTC and exchange quotes</td></tr>
<tr><td>Use</td><td>Contract fixings, refinery settlements, ETFs, central banks</td><td>Live dealing, hedging, real-time quotes</td></tr>
</table>
<p>Physical trade contracts tend to reference the benchmark because it is a single, published, auditable number for a given date &mdash; both parties can verify the fixing rather than argue over which moment's spot quote applies.</p>

<h2>How LBMA Pricing Is Used in Physical Gold Contracts</h2>
<p>A dor&eacute; or bullion contract will typically specify:</p>
<ul>
<li><strong>The reference fixing</strong> &mdash; e.g. &ldquo;the LBMA Gold Price PM fixing&rdquo;;</li>
<li><strong>The pricing date</strong> &mdash; e.g. the date of the final <a href="/knowledge/how-does-a-gold-refinery-assay-work/">assay report</a>, or an average of fixings over an agreed quotational period;</li>
<li><strong>The discount or premium</strong> &mdash; dor&eacute; settles at the benchmark applied to assayed <a href="/knowledge/what-is-fine-gold-content/">fine gold content</a>, less refining charges and the payable percentage; refined kilobars may trade at a small premium or discount to the benchmark depending on the market.</li>
</ul>

<h2>Example</h2>
<p>A contract for dor&eacute; delivered <a href="/knowledge/what-is-a-cif-gold-transaction/">CIF Dubai</a> prices at &ldquo;98.5% of the LBMA Gold Price PM fixing on the date of the final assay report, applied to assayed fine gold content&rdquo;. The assay confirms 26.86 kg fine gold (863.6 troy ounces). If the PM fixing that day is published at a given USD figure per ounce, settlement = 863.6 oz &times; fixing &times; 98.5%, less the agreed refining charges. Both parties can verify every input: the fixing is published, the assay is documented, the formula is contractual.</p>

<h2>Why the Benchmark Matters Beyond London</h2>
<p>Even gold that never touches London is priced off the London benchmark. Dubai, the world's other major physical hub, quotes premiums and discounts relative to the international price; refinery settlement schedules, off-take agreements, central bank transactions and ETF valuations all reference LBMA pricing. The LBMA's <strong>Good Delivery</strong> accreditation &mdash; the quality standard for the bars accepted in the London market &mdash; similarly anchors global expectations of what an investment-grade bar is: minimum 995.0 fineness for gold, refined by an accredited refiner.</p>
"""

TAKEAWAYS = [
    "The LBMA Gold Price is the global gold benchmark, set twice daily in London by electronic auction and quoted in USD per troy ounce.",
    "It is administered by ICE Benchmark Administration as a regulated benchmark, with accredited banks participating in the auction.",
    "Physical contracts reference the published fixing (often the PM fixing) because it is a single verifiable number for a given date.",
    "Doré settles at the benchmark applied to assayed fine gold content, less payable percentage and refining charges.",
    "LBMA Good Delivery is the companion quality standard — minimum 995.0 fineness for gold bars from accredited refiners.",
]

FAQS = [
    ("What time is the LBMA gold fixing?",
     "Twice each London business day: 10:30am (AM fixing) and 3:00pm (PM fixing), London time. Contracts usually specify which fixing applies."),
    ("Is the LBMA price the same as the spot price?",
     "No. Spot is a continuously moving dealing price; the LBMA Gold Price is a twice-daily auction benchmark. They track each other closely, but contracts reference the benchmark because it is a single published figure."),
    ("What currency is the LBMA Gold Price quoted in?",
     "US dollars per troy ounce of fine gold. ICE Benchmark Administration also publishes the price expressed in several other currencies for reference."),
    ("What is LBMA Good Delivery?",
     "The LBMA's accreditation standard for refiners and bars. A Good Delivery gold bar must meet specifications including minimum 995.0 fineness and be produced by an accredited refinery — the standard for bars traded in the London market."),
    ("Why do doré contracts settle below the LBMA price?",
     "Because doré is unrefined. Settlement applies the benchmark to assayed fine gold content, then deducts the refining and treatment charges and applies the agreed payable percentage — reflecting the cost of turning doré into saleable refined gold."),
]
