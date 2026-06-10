SLUG = "dlc-vs-sblc-explained"
TITLE = "DLC vs SBLC: What's the Difference?"
CATEGORY = "Trade Finance"
DESC = "A DLC is a primary payment mechanism paid against shipping documents; an SBLC is a backstop drawn only on default. Learn when each instrument is used in gold transactions."
CARD = "Primary payment vs safety net — how documentary and standby letters of credit differ and when gold deals use each."
ABOUT = ["Documentary letter of credit", "Standby letter of credit", "Trade finance"]
RELATED = ["what-is-an-mt700-dlc", "what-is-a-performance-bond-in-gold-trading", "what-is-a-cif-gold-transaction"]

LEAD = """<strong>A DLC (documentary letter of credit) is a primary payment mechanism: the bank pays the seller when compliant shipping and assay documents are presented. An SBLC (standby letter of credit) is a backstop: it is only drawn if the buyer fails to pay by other agreed means.</strong> Both are irrevocable bank undertakings, but they sit at opposite ends of the transaction &mdash; the DLC is <em>how the seller gets paid</em>; the SBLC is <em>what happens if payment fails</em>."""

BODY = """
<h2>The Core Difference</h2>
<p>Both instruments are issued by banks, transmitted over SWIFT, and create an independent obligation separate from the underlying sale contract. The difference is in when and why they pay:</p>
<table>
<tr><th></th><th>DLC (Documentary LC)</th><th>SBLC (Standby LC)</th></tr>
<tr><td>Purpose</td><td>Primary means of payment for the shipment</td><td>Security in case of non-payment or non-performance</td></tr>
<tr><td>Pays when</td><td>Compliant documents are presented (expected outcome)</td><td>The applicant defaults and the beneficiary demands (exceptional outcome)</td></tr>
<tr><td>Documents</td><td>Full commercial set: invoice, transport document, insurance, origin, assay</td><td>Usually a simple written demand and statement of default</td></tr>
<tr><td>Governing rules</td><td>UCP 600</td><td>ISP98 (or UCP 600 by election)</td></tr>
<tr><td>Issued via</td><td>SWIFT MT700</td><td>SWIFT MT760</td></tr>
<tr><td>Expected use</td><td>Drawn in the normal course of every shipment</td><td>Never drawn if the deal performs</td></tr>
</table>

<h2>How Each Is Used in Gold Transactions</h2>
<h3>DLC: paying for the metal</h3>
<p>In a physical gold sale &mdash; say dor&eacute; delivered <a href="/knowledge/what-is-a-cif-gold-transaction/">CIF Dubai</a> &mdash; the buyer's bank issues a <a href="/knowledge/what-is-an-mt700-dlc/">DLC via MT700</a>. The credit lists the documents the seller must present: invoice, airway bill, insurance certificate, certificate of origin and the refinery assay report. When the documents comply, the bank pays. The DLC is the payment rail of the transaction itself.</p>
<h3>SBLC: securing performance or payment</h3>
<p>An SBLC stands behind an obligation. Examples in precious metals:</p>
<ul>
<li>A buyer on open-account or contract terms provides an SBLC so the seller can draw if an invoice goes unpaid.</li>
<li>A party to a long-term <strong>off-take agreement</strong> provides an SBLC securing its commitment over multiple deliveries.</li>
<li>An SBLC can serve a similar economic role to a <a href="/knowledge/what-is-a-performance-bond-in-gold-trading/">performance bond</a>, securing a seller's obligation to deliver.</li>
</ul>
<p>If the deal performs as agreed, the SBLC simply expires undrawn.</p>

<h2>Example</h2>
<p>A refinery client contracts for monthly dor&eacute; deliveries over a year. Each monthly shipment is paid under its own sight DLC against documents. In addition, the buyer provides a 12-month SBLC for a portion of the annual contract value: if any month's payment obligation is somehow left unmet outside the credit, the seller can demand under the standby. Across the year, twelve DLC drawings occur in the normal course; the SBLC is never touched.</p>

<h2>Which Instrument Should a Deal Use?</h2>
<p>It is not either/or &mdash; the instruments answer different questions:</p>
<ul>
<li><strong>How will each shipment be paid?</strong> A DLC against documents is the established mechanism, protecting the seller (a bank must pay) and the buyer (only against documents proving shipment and assay).</li>
<li><strong>What secures performance over time, or non-payment risk outside the credit?</strong> An SBLC or guarantee.</li>
</ul>
<p>Caution is warranted in both directions: instruments described as &ldquo;leased SBLCs&rdquo; or credits issued by unverifiable banks are a recurring feature of fraudulent gold schemes. Authenticity should always be verified bank-to-bank over SWIFT, never by emailed PDFs alone.</p>
"""

TAKEAWAYS = [
    "A DLC is the primary payment mechanism, paid against compliant shipping and assay documents in the normal course of a deal.",
    "An SBLC is a standby security, drawn only if the applicant defaults — if the deal performs, it expires unused.",
    "DLCs are issued via SWIFT MT700 under UCP 600; SBLCs via MT760, usually under ISP98.",
    "Gold transactions often use both: DLCs to pay each shipment, an SBLC to secure longer-term or off-take commitments.",
    "Instrument authenticity must be verified bank-to-bank over SWIFT — emailed copies prove nothing.",
]

FAQS = [
    ("Is an SBLC stronger than a DLC?",
     "Neither is 'stronger' — they do different jobs. A DLC pays for the shipment against documents; an SBLC is a backstop against default. The strength of either depends on the issuing bank and the workability of its terms."),
    ("Can an SBLC be used to pay for gold directly?",
     "An SBLC is designed as a default instrument, not a payment rail. Structures that propose 'payment by SBLC' for physical shipments are non-standard and are frequently associated with fraudulent schemes — sellers should treat them with extreme caution."),
    ("What rules govern DLCs and SBLCs?",
     "DLCs are governed by the ICC's UCP 600. SBLCs are typically issued subject to ISP98, though they may also be issued under UCP 600. The governing rules are stated on the face of the instrument."),
    ("What is an MT760?",
     "The SWIFT message type used to issue a guarantee or standby letter of credit — the standby counterpart to the MT700 used for documentary credits."),
    ("Do SBLCs get 'leased'?",
     "'Leased' or 'rented' SBLCs marketed by brokers are a well-known hallmark of advance-fee fraud. Genuine standbys are issued by a bank for its own customer against that customer's credit facilities."),
]
