import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://metabase.ufpb.br/public/dashboard/ec8885ff-c83b-4e17-88dc-2e7253020a78?anos_cursados=&centro=&curso=&grau_acad%25C3%25AAmico=&tab=24-painel-global&turno=")
    page.get_by_role("button", name="Curso Global").click()
    page.get_by_test_id("fixed-width-filters").get_by_role("button", name="Curso").click()
    page.get_by_test_id("ADMINISTRAÇÃO-filter-value").check()
    page.get_by_role("button", name="Adicionar filtro").click()
    expect(page.get_by_text("NPS do Curso")).to_be_visible()
    page.get_by_role("button", name="Grau Acadêmico").click()
    page.get_by_test_id("BACHARELADO-filter-value").check()
    page.get_by_role("button", name="Adicionar filtro").click()
    page.locator("#mantine-fwqk84qhf-target").click()
    page.get_by_role("menuitem", name="Fazer download de resultados").click()
    with page.expect_download() as download_info:
        page.get_by_test_id("download-results-button").click()
    download = download_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
