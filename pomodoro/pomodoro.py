__version__ = "0.0.1"

import time
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--task",
        type=str,
        required=False,
        default=None,
        help="The title or name of the initial task at hand.",
    )
    parser.add_argument(
        "--task-length",
        type=int,
        required=False,
        default=25,
        help="The length, in minutes, allotted to the task as hand.",
    )
    parser.add_argument(
        "--break-length",
        type=int,
        required=False,
        default=5,
        help="The length, in minutes, allotted to each break in between each completed task.",
    )
    parser.add_argument(
        "--rest-length",
        type=int,
        required=False,
        default=15,
        help="The length, in minutes, allotted to rest periods between each completed set of tasks.",
    )
    parser.add_argument(
        "--set-count",
        type=int,
        required=False,
        default=4,
        help="The number of tasks to complete a single set before a rest period.",
    )
    parser.add_argument(
        "--disable-prompts",
        action="store_true",
        required=False,
        help="Specify this flag to disable all script prompts for input.",
    )
    args = parser.parse_args()
    task = args.task
    try:
        if task is None and not args.disable_prompts:
            task = input("[pomodoro] What is the name or title of the current task? ")
        task_completed = False
        num_tasks_completed = 0
        break_completed = False
        set_completed = False
        while True:
            if not task_completed:
                if break_completed or set_completed and not args.disable_prompts:
                    check_task = (
                        str(input(f'[pomodoro] Is the current task still "{task}" (y/n): '))
                        .lower()
                        .strip()
                    )
                    if check_task[:1] == "n":
                        task = input("[pomodoro] What is your current task? ")
                break_completed = False
                set_completed = False
                print(f"[pomodoro] Starting task: {task} ({args.task_length} min).")
                time.sleep(args.task_length * 60)
                print(f"[pomodoro] Task completed.")
                task_completed = True
                if not args.disable_prompts:
                    print(
                        "[pomodoro] Before proceeding to your break, do you have any key takeaways "
                        "or notes regarding the previously completed task?"
                    )
                    # TODO: Record this data somewhere either to a local database or csv.
                    task_notes = input()
                num_tasks_completed += 1
            if task_completed and num_tasks_completed < args.set_count:
                print(f"[pomodoro] Starting break period ({args.break_length} min).")
                time.sleep(args.break_length * 60)
                print("[pomodoro] Break completed.")
                task_completed = False
                break_completed = True
            elif task_completed and num_tasks_completed == args.set_count:
                print(f"[pomodoro] Starting rest period ({args.rest_length} min).")
                time.sleep(args.rest_length * 60)
                print("[pomodoro] Rest completed.")
                task_completed = False
                set_completed = True
                num_tasks_completed = 0
    except KeyboardInterrupt:
        pass
    finally:
        print("\n[pomodoro] Have a nice day!")
