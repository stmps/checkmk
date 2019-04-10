
// provides basic api to start and stop service

#pragma once
#ifndef windows_service_api_h__
#define windows_service_api_h__
#define WIN32_LEAN_AND_MEAN
#include <windows.h>

#include <chrono>
#include <cstdint>  // wchar_t when compiler options set weird
#include <functional>

#include "tools/_raii.h"
#include "tools/_xlog.h"

// Common Namespace for whole Windows Agent
namespace cma {

// Related to Service Agent Logic
namespace srv {
class ServiceProcessor;
int InstallMainService();                                     // on -install
int RemoveMainService();                                      // on -remove
int TestMainService(const std::wstring& What, int Interval);  // on -test
int ExecMainService(bool DuplicateOn = false);                // on -exec
int ExecStartLegacy();             // on -start_legacy
int ExecStopLegacy();              // on -stop_legacy
int ExecCap();                     // on -cap
int ExecUpgradeParam(bool Force);  // om -upgrade

int ExecSkypeTest();               // on -skype :hidden
int ExecRealtimeTest(bool Print);  // on -rt
int ExecCvtIniYaml(std::filesystem::path IniFile,
                   std::filesystem::path YamlFile,
                   bool DianosticMessages);  // on -cvt
int ExecSection(const std::wstring& SecName,
                int RepeatPause,          // if 0 no repeat
                bool DianosticMessages);  // on -section
int ServiceAsService(std::chrono::milliseconds Delay,
                     std::function<bool(const void* Processor)>
                         InternalCallback) noexcept;  // service execution

// NAMES
constexpr const wchar_t* kServiceName = L"CheckMkService";
constexpr const wchar_t* kServiceDisplayName =
    L"Check MK windows agent service";

// PARAMETERS
constexpr int kServiceStartType = SERVICE_DEMAND_START;  //  SERVICE_AUTO_START;
constexpr const wchar_t* kServiceDependencies = L"";
constexpr const wchar_t* kServiceAccount = L"NT AUTHORITY\\LocalService";
constexpr const wchar_t* kServicePassword = nullptr;

}  // namespace srv
};  // namespace cma

#endif  // windows_service_api_h__
