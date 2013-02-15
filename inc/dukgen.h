#ifndef _DUK_GENERATOR_H_
#define _DUK_GENERATOR_H_

#ifdef __cplusplus
extern "C"
{
#endif

__attribute__((visibility("hidden")))
char* GetDeviceUniqueKey(char* pAppId, int idLen, int keyLen);

#ifdef __cplusplus
}
#endif

#endif //_DUK_GENERATOR_H_



