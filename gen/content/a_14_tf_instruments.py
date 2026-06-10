SLUG = "trade-finance-instruments-in-gold-trading"
TITLE = "Trade Finance Instruments in Gold Trading"
CATEGORY = "Trade Finance"
DESC = "A reference guide to the instruments used in gold transactions — documentary credits, standbys, demand guarantees, performance bonds and the SWIFT messages that carry them."
CARD = "DLCs, SBLCs, guarantees, bonds and the SWIFT messages behind them — the full instrument toolkit, in one place."
ABOUT = ["Trade finance instruments", "Letters of credit", "Bank guarantees", "SWIFT"]
RELATED = ["what-is-an-mt700-dlc", "dlc-vs-sblc-explained", "what-is-a-performance-bond-in-gold-trading"]

LEAD = """<strong>Gold transactions are secured by a small, well-defined set of trade finance instruments: the documentary letter of credit (payment against documents), the standby letter of credit (security against default), the demand guarantee (including performance bonds), and supporting bank undertakings such as confirmations and discounting.</strong> Each is issued by a bank, transmitted over authenticated SWIFT messages, and governed by published ICC rules. Knowing which instrument does which job &mdash; and which SWIFT message carries it &mdash; is essential for structuring a workable deal."""

BODY = """
<h2>The Instrument Map</h2>
<table>
<tr><th>Instrument</th><th>Job</th><th>SWIFT</th><th>Rules</th></tr>
<tr><td>Documentary letter of credit (DLC)</td><td>Pays the seller against shipping/assay documents</td><td>MT700 (issue), MT707 (amend)</td><td>UCP 600</td></tr>
<tr><td>Standby letter of credit (SBLC)</td><td>Pays on default — security, not payment rail</td><td>MT760</td><td>ISP98 or UCP 600</td></tr>
<tr><td>Demand guarantee / performance bond</td><td>Compensates beneficiary on non-performance</td><td>MT760</td><td>URDG 758</td></tr>
<tr><td>Confirmation</td><td>Second bank adds its own payment undertaking to a DLC</td><td>Within credit terms</td><td>UCP 600</td></tr>
<tr><td>Bank comfort/capability letters</td><td>Informal indication — not an undertaking</td><td>n/a (often MT799 free format)</td><td>None — limited legal force</td></tr>
</table>

<h2>How the Instruments Combine in a Gold Deal</h2>
<p>A typical dor&eacute; transaction <a href="/knowledge/what-is-a-cif-gold-transaction/">CIF Dubai</a> stacks instruments like this:</p>
<ol>
<li><strong>The DLC pays for the metal.</strong> Issued by the buyer's bank via <a href="/knowledge/what-is-an-mt700-dlc/">MT700</a>, payable at sight against invoice, airway bill, insurance certificate, origin documents and assay report.</li>
<li><strong>The performance bond secures delivery.</strong> Issued by the seller's bank via MT760 for ~2% of contract value, claimable if the seller fails to ship &mdash; see <a href="/knowledge/what-is-a-performance-bond-in-gold-trading/">Performance Bonds Explained</a>.</li>
<li><strong>Sequencing connects them.</strong> The credit typically becomes operative on issuance of the bond (or vice versa, by negotiation) &mdash; the deal's most contested mechanic.</li>
<li><strong>Optional reinforcements.</strong> The seller may require the credit confirmed by a bank in its own jurisdiction; long-term relationships may add an SBLC securing the programme &mdash; see <a href="/knowledge/dlc-vs-sblc-explained/">DLC vs SBLC</a>.</li>
</ol>

<h2>The SWIFT Messages That Matter</h2>
<ul>
<li><strong>MT700</strong> &mdash; issues a documentary credit; carries all terms, including the critical field 46A (documents required).</li>
<li><strong>MT707</strong> &mdash; amends a credit; every amendment requires beneficiary acceptance.</li>
<li><strong>MT760</strong> &mdash; issues a guarantee or standby letter of credit.</li>
<li><strong>MT799</strong> &mdash; free-format bank-to-bank message; often used for pre-advice or comfort communications. <em>An MT799 is not a payment undertaking</em> &mdash; treating it as one is a classic error (and a classic fraud vector).</li>
</ul>

<h2>The ICC Rulebooks</h2>
<p>Instruments state on their face which rules govern them. <strong>UCP 600</strong> governs documentary credits &mdash; how banks examine documents, what compliance means, when payment is due. <strong>ISP98</strong> governs most standbys. <strong>URDG 758</strong> governs demand guarantees. These published rules are why a credit issued in one country is workable for a beneficiary in another: both sides' banks operate the same rulebook.</p>

<h2>Verification: The Non-Negotiable Step</h2>
<p>Every genuine instrument arrives through the banking system: issued by an identifiable bank, transmitted over authenticated SWIFT, and verifiable by the beneficiary's own bank. Red flags that an &ldquo;instrument&rdquo; is not real: delivery by email or courier rather than SWIFT, issuance by a non-bank &ldquo;financial institution&rdquo; nobody can verify, offers to &ldquo;lease&rdquo; instruments, MT799s presented as payment commitments, and pressure to pay fees before any authenticated message exists. A five-minute check with your own bank's trade finance desk defeats virtually all instrument fraud.</p>
"""

TAKEAWAYS = [
    "Four instruments cover gold trade: DLCs pay for shipments, SBLCs secure against default, demand guarantees/performance bonds secure delivery, confirmations add a second bank's undertaking.",
    "MT700 issues credits, MT707 amends them, MT760 issues guarantees and standbys — MT799 is free-format messaging, never a payment undertaking.",
    "Published ICC rules (UCP 600, ISP98, URDG 758) make instruments workable across borders.",
    "Sequencing between the credit and the performance bond is the most negotiated mechanic in gold contracts.",
    "Genuine instruments are verified bank-to-bank over SWIFT — anything delivered by email, 'leased', or fee-gated is presumptively fraudulent.",
]

FAQS = [
    ("What is an MT799 and is it proof of funds?",
     "A free-format bank-to-bank SWIFT message, sometimes used for pre-advice or comfort wording. It carries no payment obligation and is not proof of funds — schemes that treat MT799s as commitments are a recognised fraud pattern."),
    ("What does it mean to confirm a letter of credit?",
     "A second bank — usually in the seller's country — adds its own independent undertaking to pay against compliant documents. The seller then carries the confirming bank's risk rather than the issuing bank's."),
    ("Which ICC rules govern a standby letter of credit?",
     "Usually ISP98, though standbys can be issued subject to UCP 600. The governing rules are stated on the instrument's face."),
    ("Can these instruments be issued by non-banks?",
     "Credible instruments come from regulated banks with SWIFT access and verifiable standing. Documents issued by unverifiable 'financial institutions' or brokers have no place in a genuine gold transaction."),
    ("What is instrument 'monetisation'?",
     "A term used almost exclusively in fraudulent schemes proposing to turn standbys or guarantees into cash via 'trading programmes'. Legitimate instruments secure real transactions; they are not standalone investment products."),
]
