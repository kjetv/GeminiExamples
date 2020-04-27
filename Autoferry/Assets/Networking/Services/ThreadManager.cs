﻿using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using UnityEngine;

public class ThreadManager : MonoBehaviour
{
    private static readonly List<Action> executeOnMainThread = new List<Action>();
    private static readonly List<Action> executeCopiedOnMainThread = new List<Action>();
    private static bool actionToExecuteOnMainThread = false;

    private static readonly List<Task> runTaskOnMainThread = new List<Task>();
    private static readonly List<Task> runTaskCopiedOnMainThread = new List<Task>();
    private static bool taskToRunOnMainThread = false;

    private void Update()
    {
        UpdateMain();
    }

    /// <summary>Sets an action to be executed on the main thread.</summary>
    /// <param name="_action">The action to be executed on the main thread.</param>
    public static void ExecuteOnMainThread(Action _action)
    {
        if (_action == null)
        {
            Debug.Log("No action to execute on main thread!");
            return;
        }

        lock (executeOnMainThread)
        {
            executeOnMainThread.Add(_action);
            actionToExecuteOnMainThread = true;
        }
    }

    public static void RunTaskOnMainThread(Task _task)
    {
        if(_task == null)
        {
            Debug.Log("No task to run on main thread!");
            return;
        }

        lock (runTaskOnMainThread)
        {
            runTaskOnMainThread.Add(_task);
            taskToRunOnMainThread = true;
        }
    }

    /// <summary>Executes all code meant to run on the main thread. NOTE: Call this ONLY from the main thread.</summary>
    public static void UpdateMain()
    {
        if (actionToExecuteOnMainThread)
        {
            executeCopiedOnMainThread.Clear();
            lock (executeOnMainThread)
            {
                executeCopiedOnMainThread.AddRange(executeOnMainThread);
                executeOnMainThread.Clear();
                actionToExecuteOnMainThread = false;
            }

            for (int i = 0; i < executeCopiedOnMainThread.Count; i++)
            {
                executeCopiedOnMainThread[i]();
            }
        }

        if (taskToRunOnMainThread)
        {
            runTaskCopiedOnMainThread.Clear();
            lock(runTaskOnMainThread)
            {
                runTaskCopiedOnMainThread.AddRange(runTaskOnMainThread);
                runTaskOnMainThread.Clear();
                taskToRunOnMainThread = false;
            }

            for (int i = 0; i < runTaskCopiedOnMainThread.Count; i++)
            {
                runTaskCopiedOnMainThread[i].Start();
            }

        }
    }
}
