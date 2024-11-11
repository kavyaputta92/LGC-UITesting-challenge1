from datetime import datetime, timedelta
import time
import os
import pytest

try:
    from playwright.sync_api import sync_playwright
except ModuleNotFoundError:
    import subprocess
    subprocess.check_call(["python", "-m", "pip", "install", "playwright"])
    from playwright.sync_api import sync_playwright
import allure

# Delete previous allure screenshots before running the test
def delete_allure_screenshots():
    allure_results_path = "allure-results"
    if os.path.exists(allure_results_path):
        for file_name in os.listdir(allure_results_path):
            if file_name.endswith(".png") or file_name.endswith(".webm"):
                file_path = os.path.join(allure_results_path, file_name)
                os.remove(file_path)

delete_allure_screenshots()

@allure.feature("TODO MVC Application")
@allure.story("User can manage TODO items")
@allure.severity(allure.severity_level.CRITICAL)
def test_todo_app():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context(
            record_video_dir="videos/",
            viewport={'width': 1280, 'height': 720}
        )
        page = context.new_page()

        # Step 1: Go to the TODO MVC application
        with allure.step("Navigate to TODO MVC application"):
            page.goto("https://todomvc.com/examples/react/dist/")
            allure.attach(page.screenshot(), name="Initial Page Load", attachment_type=allure.attachment_type.PNG)

        # Step 2: Validate correct URL
        with allure.step("Validate URL"):
            assert page.url == "https://todomvc.com/examples/react/dist/"
            allure.attach(page.screenshot(), name="URL Validation", attachment_type=allure.attachment_type.PNG)

        # Step 3: Add TODO item with current date
        with allure.step("Add TODO item with today's date"):
            today_text = f"TODO 1 - {datetime.now().strftime('%Y-%m-%d')}"
            page.locator(".new-todo").fill(today_text)
            page.locator(".new-todo").press("Enter")
            allure.attach(page.screenshot(), name="After Adding TODO 1", attachment_type=allure.attachment_type.PNG)

        # Step 4: Verify new to-do item appears
        with allure.step("Verify the new TODO item appears"):
            assert page.locator(".todo-list li").first.inner_text().startswith(today_text)
            allure.attach(page.screenshot(), name="Verify TODO 1", attachment_type=allure.attachment_type.PNG)

        # Step 5: Add TODO item with tomorrow's date
        with allure.step("Add TODO item with tomorrow's date"):
            tomorrow_text = f"TODO 2 - {datetime.now() + timedelta(days=1):%Y-%m-%d}"
            page.locator(".new-todo").fill(tomorrow_text)
            page.locator(".new-todo").press("Enter")
            allure.attach(page.screenshot(), name="After Adding TODO 2", attachment_type=allure.attachment_type.PNG)

        # Step 6: Mark TODO 1 as completed
        with allure.step("Mark TODO 1 as completed"):
            page.locator(".todo-list li", has_text=today_text).locator(".toggle").click()
            allure.attach(page.screenshot(), name="Mark TODO 1 as Completed", attachment_type=allure.attachment_type.PNG)

        # Step 7: Verify item is displayed as completed
        with allure.step("Verify TODO 1 is marked as completed"):
            assert page.locator(".todo-list li.completed", has_text=today_text).is_visible()
            allure.attach(page.screenshot(), name="Verify Completed TODO 1", attachment_type=allure.attachment_type.PNG)

        # Step 8: Delete TODO 2 item
        with allure.step("Delete TODO 2 item"):
            page.locator(".todo-list li", has_text=tomorrow_text).hover()
            page.locator(".todo-list li", has_text=tomorrow_text).locator(".destroy").click(force=True)
            allure.attach(page.screenshot(), name="After Deleting TODO 2", attachment_type=allure.attachment_type.PNG)

        # Step 9: Verify TODO 2 is removed from the list
        with allure.step("Verify TODO 2 is removed"):
            assert page.locator(".todo-list li", has_text=tomorrow_text).count() == 0
            allure.attach(page.screenshot(), name="Verify TODO 2 Removed", attachment_type=allure.attachment_type.PNG)

        # Attach video to Allure report
        with allure.step("Attach test video"):
            for page in context.pages:
                video_path = page.video.path()
                context.close()
                if os.path.exists(video_path):
                    allure.attach.file(video_path, name="Test Video", attachment_type=allure.attachment_type.WEBM)

        # Cleanup
        browser.close()

if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=allure-results"])
