SLUG = "what-is-an-mt700-dlc"
TITLE = "What Is an MT700 DLC?"
CATEGORY = "Trade Finance"
DESC = "An MT700 is the SWIFT message a bank uses to issue a documentary letter of credit (DLC). Learn what the MT700 contains, how a DLC secures gold transactions, and how payment is triggered."
CARD = "The SWIFT message that issues a documentary letter of credit — what it contains and how it secures payment in gold deals."
ABOUT = ["MT700", "Documentary letter of credit", "SWIFT", "Trade finance"]
RELATED = ["dlc-vs-sblc-explained", "what-is-a-performance-bond-in-gold-trading", "what-is-a-cif-gold-transaction"]

LEAD = """<strong>An MT700 is the standard SWIFT message format that a bank uses to issue a documentary letter of credit (DLC).</strong> When traders say a deal is &ldquo;backed by an MT700 DLC&rdquo;, they mean the buyer's bank has transmitted, via the SWIFT network, a binding undertaking to pay the seller a defined amount &mdash; provided the seller presents the exact documents specified in the credit within its terms. In gold trading, the MT700 DLC is one of the principal instruments used to secure payment for physical shipments."""

BODY = """
<h2>The Two Pieces: DLC and MT700</h2>
<p>A <strong>documentary letter of credit</strong> is an irrevocable undertaking by the issuing bank to pay the beneficiary (the seller) when compliant documents are presented. The bank's promise replaces the buyer's: the seller no longer relies on the buyer choosing to pay, but on a bank obligated to pay against paper. DLCs are almost universally governed by the ICC's <strong>UCP 600</strong> rules.</p>
<p>The <strong>MT700</strong> is simply the message that brings the credit into existence between banks. SWIFT message types in the 7xx series deal with documentary credits and guarantees; the MT700 (&ldquo;Issue of a Documentary Credit&rdquo;) carries the full terms of the credit from the issuing bank to the advising bank, which authenticates it and advises the seller.</p>

<h2>What an MT700 Contains</h2>
<p>The message is built of numbered fields. The commercially important ones include:</p>
<table>
<tr><th>Field</th><th>Content</th></tr>
<tr><td>31C / 31D</td><td>Date of issue; date and place of expiry</td></tr>
<tr><td>50 / 59</td><td>Applicant (buyer) and beneficiary (seller)</td></tr>
<tr><td>32B</td><td>Currency and amount of the credit</td></tr>
<tr><td>41A / 42C</td><td>Where and how the credit is available (sight payment, deferred, acceptance)</td></tr>
<tr><td>43P / 44 series</td><td>Partial shipments, shipment route and latest shipment date</td></tr>
<tr><td>45A</td><td>Description of goods &mdash; e.g. gold dor&eacute; bars, quantity, delivery basis (CIF Dubai)</td></tr>
<tr><td>46A</td><td>Documents required for payment</td></tr>
<tr><td>47A</td><td>Additional conditions &mdash; in gold deals, often assay-related terms</td></tr>
</table>

<h2>How an MT700 DLC Works in a Gold Transaction</h2>
<ol>
<li><strong>Contract first.</strong> Buyer and seller agree the sale &mdash; quantity, quality, <a href="/knowledge/what-is-a-cif-gold-transaction/">delivery basis</a>, pricing and the documents that will trigger payment.</li>
<li><strong>Issuance.</strong> The buyer applies to its bank, which issues the DLC by sending the MT700 to the seller's advising bank.</li>
<li><strong>Advice and review.</strong> The seller's bank authenticates the message and advises the seller, who checks every field against the contract. Discrepancies are negotiated and amended (via MT707) before shipment.</li>
<li><strong>Shipment and presentation.</strong> The seller ships the gold and presents the required documents &mdash; typically invoice, airway bill, insurance certificate, certificate of origin, packing list and assay documentation.</li>
<li><strong>Examination and payment.</strong> The banks examine the documents against the credit's terms under UCP 600. If compliant, the issuing bank must pay &mdash; at sight or at the agreed tenor.</li>
</ol>

<h2>Example</h2>
<p>A refinery's client buys 50 kg of dor&eacute; CIF Dubai. The buyer's bank issues an MT700 for the contract value, available by sight payment, expiring 60 days after issue, requiring an invoice, airway bill to Dubai, insurance certificate for 110% of value, certificate of origin and a final assay report from the named refinery. The seller ships, the refinery assays, the documents are presented and found compliant, and the issuing bank pays the seller at sight &mdash; the buyer never handles the funds flow directly, and the seller never relied on the buyer's solvency alone.</p>

<h2>Why Documents — Not Gold — Trigger Payment</h2>
<p>Banks deal in documents, not goods. Under UCP 600 the bank's duty is to examine presented documents on their face for compliance; the bank does not inspect the metal. This is why precision in field 46A matters so much in gold credits: the documents listed must prove exactly what the buyer needs proven &mdash; origin, shipment, insurance and assayed content &mdash; because compliant paper means the bank must pay.</p>
"""

TAKEAWAYS = [
    "An MT700 is the SWIFT message used by an issuing bank to bring a documentary letter of credit into existence.",
    "A DLC is the issuing bank's irrevocable undertaking to pay the seller against compliant documents, governed by UCP 600.",
    "Field 46A — the required documents — is the commercial core of a gold credit: compliant paper obliges the bank to pay.",
    "Sellers should check every field of the advised MT700 against the contract before shipping; amendments travel by MT707.",
    "Banks examine documents, not goods — the assay report and shipping documents stand in for the metal itself.",
]

FAQS = [
    ("Is an MT700 the same as a letter of credit?",
     "The MT700 is the SWIFT message that issues the letter of credit. The credit is the legal undertaking; the MT700 is the authenticated format in which it is transmitted between banks."),
    ("Who pays the bank charges on a DLC?",
     "It is negotiable and stated in the credit. Commonly the applicant (buyer) pays issuance charges and each party pays its own bank's fees, but gold contracts should specify this explicitly."),
    ("What happens if documents are discrepant?",
     "The bank is not obliged to pay. It may seek the buyer's waiver of the discrepancies, or the seller may correct and re-present documents within the credit's validity. Discrepancies are the most common cause of delayed payment under DLCs."),
    ("Is an MT700 proof of funds?",
     "An authenticated MT700 evidences that a bank has issued a binding credit — substantially stronger than any 'proof of funds' letter. But its value depends on the issuing bank's standing and the workability of its terms, both of which should be verified before shipment."),
    ("Can a DLC be confirmed?",
     "Yes. A second bank (usually the seller's) can add its confirmation, taking on its own independent obligation to pay against compliant documents — useful when the seller wants payment risk held by a bank in its own jurisdiction."),
]
