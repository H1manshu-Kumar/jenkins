# Lessons learned

## Issue 1: virtualenv not activating across sh steps

Each sh step in Jenkins runs in a fresh shell. Activating virtualenv in one
step does not carry over to the next.

**Fix:** Source the activate script at the start of every sh step that needs it.

## Issue 2: Background app not ready when curl runs

The app needs ~1-2s to start. curl was failing because it ran immediately.

**Fix:** Added `sleep 2` after starting the background process.

## Issue 3: PID variable not persisting across sh steps

Saved PID in one sh step, tried to kill it in another — variable was gone.

**Fix:** Used `$!` immediately after the background start in the same sh block.
