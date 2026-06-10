SLUG = "spot-futures-and-physical-gold"
TITLE = "Spot, Futures and Physical Gold: How the Three Markets Connect"
CATEGORY = "Pricing"
DESC = "Spot is the price for immediate settlement, futures are exchange contracts for later delivery, and physical is real metal with premiums and logistics. How the three interlock."
CARD = "Three prices, one metal — how spot quotes, futures curves and physical premiums fit together."
ABOUT = ["Gold spot price", "Gold futures", "Physical gold market"]
RELATED = ["what-is-lbma-pricing", "how-international-gold-trading-works", "gold-refinery-settlement-process"]

LEAD = """<strong>Gold trades in three connected forms: the spot market (the price for metal settled now, traded over-the-counter around the clock), the futures market (standardised exchange contracts for delivery at future dates, led by COMEX in New York), and the physical market (actual bars changing hands, at premiums or discounts to the international price).</strong> The three are arbitrage-linked &mdash; they move together &mdash; but they answer different needs: spot for price discovery and dealing, futures for hedging and speculation, physical for actual metal."""

BODY = """
<h2>Spot: The Reference</h2>
<p>The spot price is the headline number &mdash; US dollars per troy ounce for immediate (conventionally two-day) settlement, discovered continuously in the over-the-counter market centred on London. Spot is primarily an institutional dealing market in unallocated metal; most spot trades never touch a physical bar. The <a href="/knowledge/what-is-lbma-pricing/">LBMA Gold Price</a> is the twice-daily auction benchmark snapshot of this market, used for contract fixings precisely because it is a single published figure.</p>

<h2>Futures: Hedging and Leverage</h2>
<p>Futures are standardised contracts &mdash; notably the COMEX 100-ounce contract &mdash; to deliver or receive gold at a future date, traded on margin through a clearing house. Producers and traders use futures to hedge: a refinery holding metal through its processing cycle, or a trader financing a shipment, can sell futures to lock value against price moves (the hedging that lenders expect, as covered in <a href="/knowledge/how-gold-transactions-are-financed/">How Gold Transactions Are Financed</a>). Speculators provide the liquidity. Although physical delivery against futures is possible, the overwhelming majority of contracts are closed or rolled before expiry &mdash; futures are a price-risk market, not a procurement channel.</p>

<h2>Physical: Real Metal, Real Logistics</h2>
<p>The physical market is where actual bars move: <a href="/knowledge/what-is-gold-dore/">dor&eacute;</a> to refineries, kilobars into regional demand, Good Delivery bars between vaults. Physical prices are quoted as premiums or discounts to the international price, reflecting local supply and demand, freight, refining capacity and bar form. Dubai kilobars, Indian imports and Shanghai prices all express this: same underlying metal, local physical conditions. Physical transactions also carry everything paper markets abstract away &mdash; <a href="/knowledge/how-gold-is-transported-securely/">logistics</a>, assay, compliance and settlement mechanics.</p>

<h2>How the Three Lock Together</h2>
<table>
<tr><th></th><th>Spot</th><th>Futures</th><th>Physical</th></tr>
<tr><td>What trades</td><td>Unallocated metal, OTC</td><td>Standardised contracts, exchange</td><td>Actual bars</td></tr>
<tr><td>Who uses it</td><td>Banks, institutions</td><td>Hedgers, speculators</td><td>Refiners, fabricators, dealers, buyers</td></tr>
<tr><td>Price expression</td><td>USD/oz, continuous</td><td>USD/oz by delivery month</td><td>Premium/discount to international price</td></tr>
<tr><td>Settlement</td><td>T+2, mostly book entry</td><td>Daily margin; rare delivery</td><td>Metal against payment</td></tr>
</table>
<p>Arbitrage keeps them aligned: if futures drift too far above spot, traders sell futures and buy spot metal to deliver; if a physical hub's premium spikes, metal flows there until it normalises. The gold price is one global price expressed three ways &mdash; with the differences (basis, premiums) carrying real information about financing costs and physical tightness.</p>

<h2>What This Means for Physical Market Participants</h2>
<ul>
<li><strong>Contracts fix against benchmarks, not screens.</strong> A dor&eacute; SPA references a published LBMA fixing &mdash; auditable by both sides &mdash; not a moving spot quote (see <a href="/knowledge/gold-purchase-agreements-key-clauses/">key contract clauses</a>).</li>
<li><strong>Premiums are part of the price.</strong> A Dubai buyer quoting &ldquo;spot plus&rdquo; or &ldquo;spot minus&rdquo; is quoting the physical basis; it moves with regional conditions.</li>
<li><strong>Hedging is available but optional.</strong> Sellers exposed between shipment and pricing date can hedge through futures or forwards — or accept the price risk knowingly. The error is not choosing; it is not realising a choice exists.</li>
</ul>
"""

TAKEAWAYS = [
    "Spot is the continuous OTC dealing price; the LBMA benchmark is its twice-daily published snapshot.",
    "Futures serve hedging and speculation on margin; most contracts never go to physical delivery.",
    "Physical metal trades at premiums or discounts to the international price reflecting local conditions and bar form.",
    "Arbitrage links all three — one global gold price, three expressions.",
    "Physical contracts should fix against published benchmarks; premiums and hedging decisions are part of deal economics.",
]

FAQS = [
    ("Why is the futures price different from spot?",
     "The difference (basis) mainly reflects financing and storage costs to the delivery date. Gold futures normally trade above spot (contango); the gap narrows toward expiry."),
    ("Can you take delivery of gold from a futures contract?",
     "On COMEX, yes — standardised bars through approved depositories, for the small minority who choose it. It is a financial market mechanism, not a practical procurement route for most physical buyers."),
    ("What is unallocated vs allocated gold?",
     "Unallocated is a claim on a bullion bank's general metal pool — credit exposure, no specific bars. Allocated is identified bars held in custody for you. Most spot dealing is unallocated; physical settlement and vaulting can be allocated."),
    ("What does 'spot plus two' mean in a physical quote?",
     "A premium of two dollars per ounce over the spot/benchmark price — the physical basis for that product in that market at that time."),
    ("Should a doré seller hedge between shipment and pricing?",
     "It depends on the pricing clause and risk appetite. If the contract prices at a future assay date, the seller carries market risk until then and can hedge it with futures or forwards — a deliberate commercial decision, ideally made before shipment."),
]
