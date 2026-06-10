SLUG = "gold-refinery-settlement-process"
TITLE = "The Gold Refinery Settlement Process"
CATEGORY = "Refining"
DESC = "How refineries pay for gold: net melt weight × assay = fine content; payable percentage applied; priced at the benchmark fixing; charges deducted; paid within the contractual window."
CARD = "From assay result to money in the bank — every step and deduction in a refinery settlement, worked through."
ABOUT = ["Refinery settlement", "Gold settlement", "Payable gold"]
RELATED = ["how-does-a-gold-refinery-assay-work", "what-is-fine-gold-content", "what-is-lbma-pricing"]

LEAD = """<strong>The gold refinery settlement process converts an assayed delivery into payment: net melt weight multiplied by assayed purity gives fine gold content; the contractual payable percentage is applied; the result is priced against the agreed benchmark fixing; refining, treatment and assay charges are deducted; and the balance is paid within the contractual settlement window.</strong> Every element is documented and verifiable &mdash; which is precisely what makes refinery settlement bankable."""

BODY = """
<h2>The Settlement Formula</h2>
<p>Settlement value = (net melt weight &times; assay result) &times; payable % &times; benchmark price &minus; charges</p>
<p>Five inputs, each independently evidenced:</p>
<ol>
<li><strong>Net melt weight</strong> &mdash; recorded after the lot is melted to homogeneity, witnessed where the contract provides.</li>
<li><strong>Assay result</strong> &mdash; the refinery laboratory's purity determination, checked against the seller's split sample &mdash; see <a href="/knowledge/how-does-a-gold-refinery-assay-work/">How Does a Gold Refinery Assay Work?</a></li>
<li><strong>Payable percentage</strong> &mdash; the contractual share of fine content paid for, commonly 98&ndash;99.5% for gold.</li>
<li><strong>Benchmark price</strong> &mdash; usually a named <a href="/knowledge/what-is-lbma-pricing/">LBMA fixing</a> on a defined date (assay date, or an average over a quotational period).</li>
<li><strong>Charges</strong> &mdash; the agreed schedule: refining charge per kilogram, treatment charges for problematic elements, assay fees, and any handling costs.</li>
</ol>

<h2>A Worked Settlement</h2>
<p>A 25 kg dor&eacute; lot delivered <a href="/knowledge/what-is-a-cif-gold-transaction/">CIF Dubai</a>:</p>
<table>
<tr><th>Step</th><th>Figure</th></tr>
<tr><td>Net melt weight</td><td>24.96 kg</td></tr>
<tr><td>Assay (gold)</td><td>91.3%</td></tr>
<tr><td>Fine gold content</td><td>22.79 kg (732.7 troy oz)</td></tr>
<tr><td>Payable at 99%</td><td>22.56 kg (725.4 troy oz)</td></tr>
<tr><td>Priced at LBMA PM fixing, assay date</td><td>725.4 oz &times; fixing</td></tr>
<tr><td>Less refining charges (per agreed schedule)</td><td>&minus; charges</td></tr>
<tr><td>Plus silver credit (assayed, per agreement)</td><td>+ credit</td></tr>
<tr><td><strong>Settlement paid</strong></td><td><strong>within contractual window of final assay</strong></td></tr>
</table>

<h2>Payment Mechanics</h2>
<p>Settlement is paid by bank transfer to the seller's nominated account, or &mdash; where the transaction is financed &mdash; through the governing <a href="/knowledge/what-is-an-mt700-dlc/">letter of credit</a>, with the final assay report among the documents presented for payment. Some agreements offer <strong>provisional settlement</strong>: a large percentage (for example 90%) paid promptly on preliminary assay, with the balance on final assay &mdash; valuable for seller cash flow on larger lots. Alternatively, sellers may take <strong>metal account credit</strong> &mdash; fine ounces credited to an account at the refinery &mdash; and sell or withdraw later, separating the metal decision from the price decision.</p>

<h2>Where Settlements Go Wrong</h2>
<ul>
<li><strong>Assay disputes</strong> &mdash; resolved by the contract's umpire mechanism; absent one, the seller has little leverage after delivery.</li>
<li><strong>Ambiguous pricing dates</strong> &mdash; &ldquo;market price&rdquo; without a named fixing and date invites dispute; precise quotational language prevents it.</li>
<li><strong>Unscheduled charges</strong> &mdash; deductions not in the agreed schedule. The remedy is a complete written schedule of charges before shipment.</li>
<li><strong>Slow payment</strong> &mdash; the agreement should state a payment deadline running from final assay, not an open-ended &ldquo;after processing&rdquo;.</li>
<li><strong>By-metal silence</strong> &mdash; high-silver dor&eacute; without a silver-credit clause gives away real value.</li>
</ul>

<h2>Why This Process Is Bankable</h2>
<p>Every input to a refinery settlement is independently verifiable: calibrated weights, laboratory assays with split samples, a published benchmark, a written schedule of charges. That auditability is why banks finance metal through the refining cycle and why refinery settlement documents satisfy letters of credit &mdash; and it is the standard a seller should hold every settlement to. If any input can't be evidenced, the settlement isn't finished.</p>
"""

TAKEAWAYS = [
    "Settlement = net melt weight × assay × payable % × benchmark price − charges, with every input independently documented.",
    "Pricing should name the exact fixing and date (or quotational period) — ambiguity here is the most common settlement dispute.",
    "Provisional settlement and metal account credit are useful options for cash flow and price timing.",
    "A complete written schedule of charges before shipment prevents unscheduled deductions after it.",
    "By-metal credits — especially silver in high-silver doré — belong in the agreement, not in the refinery's discretion.",
]

FAQS = [
    ("How quickly does a refinery pay after assay?",
     "Per the agreement — commonly within one to several business days of final assay for established relationships, and on presentation of compliant documents where a letter of credit governs payment."),
    ("What is provisional settlement?",
     "An advance — often around 90% of estimated value — paid promptly on preliminary assay, with the balance settled on final assay. It accelerates seller cash flow on larger lots."),
    ("What is a metal account?",
     "An account at the refinery denominated in fine ounces or grams. Sellers can take settlement as metal credit and sell or withdraw later, separating delivery timing from pricing timing."),
    ("Can the seller choose the pricing date?",
     "Within what the contract allows. Some agreements let the seller call the pricing within a quotational window; others fix it mechanically to the assay date. Either way, it must be defined in advance."),
    ("Are refining charges negotiable?",
     "Yes — they vary with volume, purity profile, contaminants and relationship. Larger, cleaner, regular flows command better schedules. The essential point is that whatever is agreed is written before shipment."),
]
