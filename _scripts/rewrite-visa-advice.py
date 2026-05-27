import re

with open('lifestyle/thai-visa-advice.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

NEW_BODY = """<div class="blog-body">

                    <!-- TL;DR IMAGE + SUMMARY -->
                    <figure class="img-right-small" style="margin-top: -30px; margin-bottom: 1rem; width: calc(100% - 400px); max-width: 280px;">
                        <img src="../images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp" alt="Thai visa options for expats in Chiang Mai" width="280" height="210" loading="lazy">
                    </figure>
                    <div class="article-sidebar">
                        <h4>Quick Summary (TL;DR)</h4>
                        <ul>
                            <li>Just arrived and want to extend your 30-day stamp? Apply for a 30-day extension at Promenada Immigration (1,900 THB).</li>
                            <li>Staying 2-3 months? A Tourist Visa (TR) gives you 60 days plus a 30-day extension.</li>
                            <li>Remote worker or digital nomad? The DTV Visa gives 180-day stays. No work permit required for foreign-source income.</li>
                            <li>Studying Thai, Muay Thai, or another discipline? The ED Visa covers up to 1 year with school enrolment.</li>
                            <li>Retired (50+) with income or savings? The Retirement Visa (OA) is the most stable long-term option.</li>
                            <li>Married to a Thai national? The Marriage Visa is renewable annually.</li>
                            <li>For every visa: CMA explains what it is. CMLocals explains how to get it.</li>
                        </ul>
                    </div>

                    <h2>Visa Exempt Entry (30-60 days)</h2>

                    <p>Most nationalities enter Thailand without a visa for 30 days (recently extended to 60 days for many). This is not a visa. It is a stamp. You cannot renew it inside Thailand. You can extend it once at Promenada Immigration for 30 days (1,900 THB). After that, you need to leave and re-enter, or switch to a proper visa.</p>

                    <p>The terminology matters. You are not on a "tourist visa." You are on a visa exempt entry. You do not renew a visa inside Thailand, you apply for an extension of stay. If you leave to get another stamp, you are border-bouncing. If you go to a Thai consulate to buy a new visa, you are doing a visa run. These are different things and the distinction matters at Immigration.</p>

                    <p>See the full breakdown: <a href="../visa/visa-exempt-vs-voa.html">Visa Exempt vs Visa on Arrival</a></p>

                    <div class="callout-info">
                        <p><strong>Ready to apply?</strong> Full step-by-step guide, extension process, and current processing times at <a href="https://cmlocals.com/visa-exempt/" target="_blank" rel="noopener">CMLocals: Visa Exempt Guide</a>.</p>
                    </div>

                    <h2>Tourist Visa (TR, 60 days)</h2>

                    <p>A Tourist Visa is purchased at a Thai consulate before you arrive, or via the Thai e-Visa system online. It gives 60 days on arrival, extendable for 30 more days at Immigration (1,900 THB). Total: up to 90 days in Thailand.</p>

                    <p>Multiple-entry tourist visas (METV) allow 6 months of visits with each stay capped at 60 days. Good for people who want flexibility without committing to a longer visa category. Not ideal if you plan to stay more than 3 months continuously.</p>

                    <p>See more: <a href="../visa/tourist-visa.html">Tourist Visa overview</a></p>

                    <div class="callout-info">
                        <p><strong>Ready to apply?</strong> Full step-by-step guide, consulate list, and e-Visa instructions at <a href="https://cmlocals.com/tourist-visa/" target="_blank" rel="noopener">CMLocals: Tourist Visa Guide</a>.</p>
                    </div>

                    <h2>DTV Visa (Destination Thailand Visa, 180 days)</h2>

                    <p>Launched in 2024, the DTV is Thailand's answer to the digital nomad visa. One 180-day entry per use, with multiple entries allowed on the same visa over 5 years. No work permit needed for income earned outside Thailand.</p>

                    <p>Requirements: proof of remote work or freelance income, and either 500,000 THB in savings or equivalent monthly income. Cost: 10,000 THB. Apply online via the Thai e-Visa portal. Best option for location-independent workers who want flexibility without the annual reporting obligations of an ED or retirement visa.</p>

                    <p>See more: <a href="../visa/dtv-visa.html">DTV Visa overview</a></p>

                    <div class="callout-info">
                        <p><strong>Ready to apply?</strong> Full application walkthrough, document checklist, and current processing times at <a href="https://cmlocals.com/dtv-visa/" target="_blank" rel="noopener">CMLocals: DTV Visa Guide</a>.</p>
                    </div>

                    <h2>ED Visa (Education, up to 1 year)</h2>

                    <p>The ED Visa covers genuine study at a Ministry of Education-registered institution. Thai language, Muay Thai, martial arts, and yoga all qualify if the school is properly registered. You get 90 days initially, extendable for 90 more at Immigration while enrolled. Total: up to 1 year per enrolment.</p>

                    <p>The school handles your paperwork. You show up, study, and report to Airport Road Immigration every 90 days. Choose your school carefully. Some are visa mills with no real curriculum. A reputable school will ask about your genuine study goals.</p>

                    <p>See more: <a href="../visa/ed-visa.html">ED Visa overview</a> | <a href="../visa/ed-visa-thai-language.html">Thai Language</a> | <a href="../visa/ed-visa-muay-thai.html">Muay Thai</a></p>

                    <div class="callout-info">
                        <p><strong>Ready to apply?</strong> School recommendations, document checklist, and extension process at <a href="https://cmlocals.com/ed-visa/" target="_blank" rel="noopener">CMLocals: ED Visa Guide</a>.</p>
                    </div>

                    <h2>Retirement Visa (OA / OX, age 50+)</h2>

                    <p>Available to anyone 50 or older. The OA requires either 800,000 THB seasoned in a Thai bank account or proof of monthly pension/income of 65,000 THB. Annual renewal at Promenada Immigration. You must report your address every 90 days.</p>

                    <p>The OX is a 10-year long-stay version with higher financial requirements. The Retirement Visa is the most administratively stable option for long-term residents who qualify by age and finances.</p>

                    <p>See more: <a href="../visa/retirement-visa.html">Retirement Visa overview</a></p>

                    <div class="callout-info">
                        <p><strong>Ready to apply?</strong> Full requirements, bank seasoning rules, and renewal process at <a href="https://cmlocals.com/retirement-visa/" target="_blank" rel="noopener">CMLocals: Retirement Visa Guide</a>.</p>
                    </div>

                    <h2>Marriage Visa (Non-Immigrant O)</h2>

                    <p>For foreign nationals legally married to a Thai citizen. Gives 1 year stay, renewable annually at Promenada Immigration. Financial requirement: 400,000 THB in a Thai bank account or monthly income of 40,000 THB. You must report your address every 90 days.</p>

                    <p>The most administratively straightforward long-term option if you qualify. Less financial burden than Retirement, no study commitment like ED, no income proof requirement like DTV.</p>

                    <p>See more: <a href="../visa/marriage-visa.html">Marriage Visa overview</a></p>

                    <div class="callout-info">
                        <p><strong>Ready to apply?</strong> Full requirements, marriage documentation, and renewal process at <a href="https://cmlocals.com/marriage-visa/" target="_blank" rel="noopener">CMLocals: Marriage Visa Guide</a>.</p>
                    </div>

                    <h2>LTR Visa (Long-Term Resident, 10 years)</h2>

                    <p>Thailand's premium visa for wealthy retirees, high-earning remote workers, and highly skilled professionals. Four categories: Wealthy Global Citizen (1M USD in assets), Wealthy Pensioner (80,000 USD/year), Work-From-Thailand Professional (40,000 USD/year), and Highly Skilled Professional (BOI-approved industries).</p>

                    <p>Benefits include exemption from 90-day reporting and a 17% flat income tax rate on Thai-source income. If you qualify, it is the smoothest long-term option available.</p>

                    <p>See more: <a href="../visa/ltr-visa.html">LTR Visa overview</a></p>

                    <div class="callout-info">
                        <p><strong>Ready to apply?</strong> Eligibility criteria, application process, and benefits breakdown at <a href="https://cmlocals.com/ltr-visa/" target="_blank" rel="noopener">CMLocals: LTR Visa Guide</a>.</p>
                    </div>

                    <h2>The Thai Visa Advice Facebook Group</h2>

                    <p>For real-time questions, edge cases, and situations that do not fit neatly into any of the above categories, the <a href="https://www.facebook.com/groups/1395920320731833/" rel="noopener" target="_blank">Thai Visa Advice Facebook Group</a> is the most reliable community resource in existence.</p>

                    <p>The admins work with Immigration daily. They understand the latest policy changes, regional variations, and the reality that different officers interpret the same rules differently. Their advice is generally better than what you will get from a lawyer who does not specialise in Thai immigration.</p>

                    <p>A few key terminology points: there is no such thing as a 30-day tourist visa (it is a visa exempt stamp). You never renew a visa inside Thailand, you extend your stay. Border-bouncing and visa-running are different activities. Get the language right before you walk into Immigration.</p>

                    <p><strong>Last verified: May 2026</strong></p>

                </div>
            </div>
        </article>"""

new_content = re.sub(
    r'<div class="blog-body">.*?</div>\s*\r?\n\s*</div>\s*\r?\n\s*</article>',
    NEW_BODY,
    content,
    flags=re.DOTALL
)

if new_content == content:
    print('ERROR: No replacement made')
else:
    with open('lifestyle/thai-visa-advice.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Done - replaced blog-body content')
