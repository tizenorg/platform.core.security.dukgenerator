//
// Copyright (c) 2013 Samsung Electronics Co., Ltd.
//
// Licensed under the Apache License, Version 2.0 (the License);
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <openssl/evp.h>
#include <openssl/rand.h>
#include <SecCryptoSvc.h>
#include <dukgen.h>

char* GetDeviceUniqueKey(char* pAppId, int idLen, int keyLen)
{
	unsigned char* pUniqueKey = NULL;
	char* pDuk = NULL;
	bool result = true;

	pUniqueKey = (unsigned char*)calloc(keyLen,1);
	if (pUniqueKey == NULL)
		return NULL;
	result = SecFrameGeneratePlatformUniqueKey((unsigned int)keyLen , pUniqueKey);
	if(result == false)
	{
		free(pUniqueKey);
		return NULL;
	}

	pDuk = (char*)calloc(keyLen, 1);
	if (pDuk == NULL)
	{
		free(pUniqueKey);
		return NULL;
	}
	PKCS5_PBKDF2_HMAC_SHA1(pAppId, idLen, (unsigned char*)pUniqueKey, keyLen, 1, keyLen, (unsigned char*)pDuk);
	free(pUniqueKey);

	return pDuk;
}
