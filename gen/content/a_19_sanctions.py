SLUG = "sanctions-compliance-for-precious-metals"
TITLE = "Sanctions Compliance for Precious Metals"
CATEGORY = "Compliance"
DESC = "Sanctions regimes prohibit dealing with listed parties, banks and origins — including specific bans on gold of certain origins. How sanctions screening works in gold transactions."
CARD = "Listed parties, banned origins, blocked banks — the screening that must clear before any gold deal proceeds."
ABOUT = ["Sanctions", "Sanctions screening", "Precious metals compliance"]
RELATED = ["gold-aml-requirements", "kyc-procedures-in-precious-metals", "responsible-gold-sourcing"]

LEAD = """<strong>Sanctions compliance in precious metals means ensuring that no party, bank, vessel, route or origin connected to a transaction is subject to applicable sanctions</strong> &mdash; including the specific prohibitions several regimes apply to gold itself, such as bans on gold of particular national origin. Sanctions are strict-liability in many jurisdictions: intent does not matter, exposure anywhere in the chain can taint a transaction, and banks will freeze rather than process doubtful flows. Screening therefore runs before, and throughout, every gold transaction."""

BODY = """
<h2>What Can Be Sanctioned in a Gold Deal</h2>
<ul>
<li><strong>Parties</strong> &mdash; sellers, buyers, intermediaries, their beneficial owners and controllers, against lists such as the UN consolidated list, the US OFAC SDN list, and UK and EU regimes.</li>
<li><strong>Banks</strong> &mdash; an instrument issued or advised through a sanctioned or restricted bank cannot be processed by compliant counterparts.</li>
<li><strong>Origins</strong> &mdash; several regimes prohibit gold of specific national origin outright; origin verification is therefore a sanctions matter, not only a <a href="/knowledge/responsible-gold-sourcing/">responsible-sourcing</a> one.</li>
<li><strong>Carriers and routes</strong> &mdash; sanctioned airlines, vessels or transit arrangements can taint otherwise clean shipments.</li>
<li><strong>Activities</strong> &mdash; sectoral measures can restrict dealings connected to particular industries or governments even where parties are not individually listed.</li>
</ul>

<h2>Why Gold Gets Specific Attention</h2>
<p>Gold is a sanctions-evasion asset of choice: it stores massive value outside the banking system, crosses borders physically, and can be remelted to disguise origin. Regulators know this &mdash; which is why recent regimes have targeted gold explicitly and why enforcement attention on the sector is high. Remelting sanctioned-origin gold does not cleanse it legally; transformations designed to disguise origin are themselves evasion.</p>

<h2>How Screening Works in Practice</h2>
<ol>
<li><strong>At KYC.</strong> Every party and beneficial owner identified during <a href="/knowledge/kyc-procedures-in-precious-metals/">KYC</a> is screened against current lists. A confirmed match ends the matter &mdash; there is no commercial workaround for a listed party.</li>
<li><strong>At instrument issuance.</strong> Banks screen all parties, banks and goods descriptions before issuing or advising a <a href="/knowledge/what-is-an-mt700-dlc/">letter of credit</a>; sanctions clauses in credits address supervening restrictions.</li>
<li><strong>At shipment.</strong> Origin documents, carrier and routing are checked against origin-based prohibitions and listed operators.</li>
<li><strong>Continuously.</strong> Lists change weekly. Ongoing relationships and in-flight transactions are rescreened; a party listed mid-transaction freezes the transaction.</li>
</ol>

<h2>Example</h2>
<p>A buyer is offered attractive dor&eacute; volumes through a new intermediary. Screening clears the intermediary entity &mdash; but beneficial ownership analysis reveals a 50% shareholder who is a listed person under an applicable regime. Under ownership-and-control rules, the entity itself is treated as sanctioned. The transaction is declined and, where required, reported. Note the mechanism: the entity appeared clean; only the look-through to beneficial owners exposed the prohibition &mdash; which is why KYC depth and sanctions compliance are inseparable.</p>

<h2>Practical Rules for Gold Market Participants</h2>
<ul>
<li><strong>Screen everyone, including banks and carriers</strong> &mdash; not just the counterparty's name.</li>
<li><strong>Verify origin independently</strong> &mdash; origin-based gold bans make &ldquo;where is this metal actually from?&rdquo; a legal question with strict-liability consequences.</li>
<li><strong>Watch for evasion patterns</strong> &mdash; transhipment through third countries, recently re-papered origin, remelted bars without history, and intermediaries with opaque ownership.</li>
<li><strong>Document the screening</strong> &mdash; regulators and banks expect evidence that checks were run and resolved, not assurances.</li>
<li><strong>When in doubt, stop</strong> &mdash; sanctions exposure is one of the few risks in gold trading with no commercial mitigation. Doubt is a reason to halt, escalate and take advice.</li>
</ul>
"""

TAKEAWAYS = [
    "Sanctions can attach to parties, beneficial owners, banks, carriers, routes and the gold's national origin itself.",
    "Several regimes ban gold of specific origins outright — origin verification is a strict-liability legal requirement.",
    "Remelting or re-papering sanctioned gold does not cleanse it; disguising origin is itself evasion.",
    "Screening runs at KYC, at instrument issuance, at shipment and continuously — lists change weekly.",
    "Ownership-and-control rules mean a clean-looking entity can be sanctioned through its shareholders — look through to people.",
]

FAQS = [
    ("Whose sanctions apply to a gold transaction?",
     "Potentially several regimes at once: those of each party's jurisdiction, the currency used (US dollar transactions engage US jurisdiction), the banks involved, and transit points. Compliant practice screens against all plausibly applicable lists."),
    ("Is gold from a sanctioned country always prohibited?",
     "Where a regime imposes an origin-based gold ban, yes for persons subject to that regime — regardless of who sells it or where it was refined. Precise scope depends on each regime's terms, which is why origin evidence matters so much."),
    ("Does refining sanctioned gold in a third country make it legal?",
     "No. Transformation undertaken to disguise sanctioned origin is evasion, and regulators have pursued exactly this pattern in the gold sector."),
    ("What happens if a party is sanctioned mid-transaction?",
     "Compliant banks freeze the transaction and funds per their obligations. This is why sanctions clauses appear in credits and contracts, and why continuous rescreening of live transactions is standard."),
    ("What is the difference between sanctions and AML obligations?",
     "AML targets criminal proceeds and requires risk-based controls and reporting. Sanctions are prohibitions against dealing with listed parties and activities — typically strict liability, with no risk-based discretion for confirmed matches. Gold compliance programmes must run both."),
]
