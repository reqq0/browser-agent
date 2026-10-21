from playwright.async_api import Page

async def page_state(page:Page):
    js = """
    function () {
        document.querySelectorAll('[target-id]').forEach(function (element) {
            element.removeAttribute('target-id');
        });

        let id = 1;
        let contextText = '';
        const elements = document.querySelectorAll(
            'button, a, input, textarea, select, [role="button"], [role="link"]'
        );

        elements.forEach(function (element) {
            const rect = element.getBoundingClientRect();
            const style = getComputedStyle(element);
            if (
                rect.width === 0 ||
                rect.height === 0 ||
                style.visibility === 'hidden' ||
                style.display === 'none'
            ) {
                return;
            }

            element.setAttribute('target-id', id);
            const tagName = element.tagName.toLowerCase();
            const type = element.getAttribute('type') || '';
            const placeholder = element.getAttribute('placeholder') || '';
            const text = (
                element.innerText ||
                element.value ||
                element.getAttribute('aria-label') ||
                ''
            ).trim();
            let description = `<${tagName}`;
            if (type) description += ` type="${type}"`;
            if (placeholder) description += ` placeholder="${placeholder}"`;
            description += '>';
            if (text) description += ` ${text.substring(0, 60)}`;

            contextText += `[${id}] ${description}\n`;
            id++;
        });

        return contextText;
    }

         """
    state = await page.evaluate(js)
    return f"Current URL: {page.url}\n\nInteractive Elements:\n{state}"